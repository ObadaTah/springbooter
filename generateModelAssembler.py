def generateModelAssembler(path, className, packageName):
    classFile = open(path + "ModelAssembler.java", "w")
    data = (
        packageName
        + """\n
    import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.*;

import org.springframework.hateoas.EntityModel;
import org.springframework.hateoas.server.RepresentationModelAssembler;
import org.springframework.stereotype.Component;

@Component
class """
        + className
        + """ModelAssembler implements RepresentationModelAssembler<"""
        + className
        + """, EntityModel<"""
        + className
        + """>> {

        @Override
        public EntityModel<"""
        + className
        + """> toModel("""
        + className
        + """ """
        + className.lower()
        + """) {

                return EntityModel.of(
                                """
        + className.lower()
        + """, //
                                linkTo(methodOn(
                                                """
        + className
        + """Controller.class).one(
                                                                """
        + className.lower()
        + """.getId()))
                                                .withSelfRel(),
                                linkTo(methodOn("""
        + className
        + """Controller.class).all()).withRel(
            "+"""
        + className.lower()
        + """s"));
        }

}
    
    
    """
    )
    classFile.write(data)
    classFile.close()
