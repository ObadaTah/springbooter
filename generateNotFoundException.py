def generateNotFoundException(path, className):
    classFile = open(path + "NotFoundException.java", "w")
    data = (
        """"
    
public class """
        + className
        + """NotFoundException extends RuntimeException {

  public """
        + className
        + """NotFoundException(Long id) {
    super("Could not find """
        + className
        + """ + id);
  }
}

    """
    )

    classFile.write(data)
    classFile.close()
