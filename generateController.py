def generateController(path, className, attr, packageName):
    classFile = open(path + "Controller.java", "w")
    data = (
        packageName
        + """
    \n
import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.*;

import java.util.List;
import java.util.stream.Collectors;
import org.springframework.http.*;

import org.springframework.hateoas.*;
import org.springframework.web.bind.annotation.*;


@RestController
public class """
        + className
        + "Controller {\n"
        + """
private final """
        + className
        + """Repository repository;
    private final """
        + className
        + """ModelAssembler assembler;
    """
        + className
        + """Controller("""
        + className
        + """Repository repository, """
        + className
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
        + className
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
        + className
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
    }
"""
    )
    classFile.write(data)
