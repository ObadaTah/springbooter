def generateNotFoundAdvice(path, className, packageName):
    classFile = open(path + "NotFoundAdvice.java", "w")
    data = (
        packageName
        + """
    \n
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;

@ControllerAdvice
public class """
        + className
        + """NotFoundAdvice {

  @ResponseBody
  @ExceptionHandler("""
        + className
        + """NotFoundException.class)
  @ResponseStatus(HttpStatus.NOT_FOUND)
  String """
        + className.lower()
        + """NotFoundHandler("""
        + className
        + """NotFoundException ex) {
    return ex.getMessage();
  }
}
    """
    )
    classFile.write(data)
    classFile.close()
