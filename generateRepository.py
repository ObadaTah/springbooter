def generateRepository(path, className, packageName):
    classFile = open(path + "Repository.java", "w")
    data = (
        packageName
        + """
    \n
import org.springframework.data.jpa.repository.JpaRepository;

public interface """
        + className
        + """Repository extends JpaRepository<"""
        + className
        + """, Long> {

}

    
    """
    )

    classFile.write(data)
    classFile.close()
