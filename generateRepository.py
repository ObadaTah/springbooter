def generateRepository(path, className):
    classFile = open(path + "Repository.java", "w")
    data = (
        """
    
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
