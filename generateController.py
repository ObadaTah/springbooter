def generateController(path, className, attr):
    classFile = open(path + "Controller.java", "w")
    data = (
        """
    
import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.linkTo;
import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.methodOn;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.hateoas.CollectionModel;
import org.springframework.hateoas.EntityModel;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;


@RestController
public class """
        + className.lower()
        + "Controller {\n"
        + """
private final """
        + className.lower()
        + """ Repository repository;
    private final """
        + className.lower()
        + """ModelAssembler assembler;
    """
        + className.lower()
        + """Controller("""
        + className.lower()
        + """Repository repository, """
        + className.lower()
        + """ModelAssembler assembler) {
        this.repository = repository;
        this.assembler = assembler;
    }
    
    @GetMapping("/"""
        + className.lower()
        + """s/{"""
        + className.lower()
        + """Id}")
    EntityModel<"""
        + className
        + """> one(@PathVariable Long """
        + className.lower()
        + """Id) {

        """
        + className
        + """ """
        + className.lower()
        + """ = repository.findById("""
        + className.lower()
        + """Id)
                .orElseThrow(() -> new """
        + className
        + """NotFoundException("""
        + className.lower()
        + """Id));

        return assembler.toModel("""
        + className.lower()
        + """);
    }
    
     @GetMapping("/"""
        + className.lower()
        + """s")
    CollectionModel<EntityModel<"""
        + className
        + """>> all() {
        List<EntityModel<"""
        + className
        + """>> """
        + className.lower()
        + """s = repository.findAll().stream().map("""
        + className.lower()
        + """ -> assembler.toModel("""
        + className.lower()
        + """))
                .collect(Collectors.toList());

        return CollectionModel.of("""
        + className.lower()
        + """s, linkTo(methodOn("""
        + className
        + """Controller.class).all()).withSelfRel());
    }
    
    
     @PostMapping("/"""
        + className.lower()
        + """s")
  ResponseEntity<?> new"""
        + className
        + """(@RequestBody """
        + className
        + """ new"""
        + className
        + """) {

    EntityModel<"""
        + className
        + """> entityModel = assembler.toModel(repository.save(new"""
        + className
        + """));

    return ResponseEntity.created(entityModel.getRequiredLink(IanaLinkRelations.SELF).toUri()).body(entityModel);
  }
  
  @PutMapping("/"""
        + className.lower()
        + """s/{id}")
  ResponseEntity<?> edit"""
        + className
        + """(@RequestBody """
        + className
        + """ new"""
        + className
        + """, @PathVariable Long id) {

    return repository.findById(id)
        .map("""
        + className.lower()
        + """ -> {"""
    )
    for i in attr.keys():
        data += (
            className.lower()
            + ".set"
            + i.capitalize()
            + "(new"
            + className
            + ".get"
            + i.capitalize()
            + "());\n"
        )

    data += (
        """ EntityModel<"""
        + className.lower()
        + """> entityModel = assembler.toModel(repository.save("""
        + className.lower()
        + """));
          return ResponseEntity.created(entityModel.getRequiredLink(IanaLinkRelations.SELF).toUri()).body(entityModel);
        })
        .orElseGet(() -> {
          new"""
        + className
        + """.setId(id);
          EntityModel<"""
        + className.lower()
        + """> entityModel = assembler.toModel(repository.save(new"""
        + className
        + """));
          return ResponseEntity.created(entityModel.getRequiredLink(IanaLinkRelations.SELF).toUri()).body(entityModel);
        });
  }
  
  @DeleteMapping("/"""
        + className.lower()
        + """s/{id}")
  ResponseEntity<?> delete"""
        + className
        + """(@PathVariable Long id) {

    """
        + className
        + """ """
        + className.lower()
        + """ = repository.findById(id).orElseThrow(() -> new """
        + className
        + """NotFoundException(id));

    repository.delete("""
        + className.lower()
        + """);

    return ResponseEntity.noContent().build();

  }
    
"""
    )
    classFile.write(data)
