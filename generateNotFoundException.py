def generateNotFoundException(path, className, packageName):
    classFile = open(path + "NotFoundException.java", "w")
    data = (
        packageName
        + """
    \n
public class """
        + className
        + """NotFoundException extends RuntimeException {

  public """
        + className
        + """NotFoundException(Long id) {
    super("Could not find """
        + className
        + """" + id);
  }
}

    """
    )

    classFile.write(data)
    classFile.close()
