def generateClass(path, className, attr):
    classFile = open(path + ".java", "w")
    data = (
        """import jakarta.persistence.Entity;
    import jakarta.persistence.GeneratedValue;
    import jakarta.persistence.Id;
    import lombok.Data;

    @Data
    @Entity
    public class """
        + className
        + "{\n"
        + "private @Id @GeneratedValue Long id;\n"
    )

    for i in attr.keys():
        data += "private " + attr[i] + " " + i + ";\n"

    data += "public " + className + "("
    for i in attr.keys():
        data += attr[i] + " " + i + ", "
    data += " "
    data = data.replace(",  ", "")
    data += "){\n"
    for i in attr.keys():
        data += "this." + i + " = " + i + "; \n"
    data += "}"
    data += "public " + className + "() { } }"
    classFile.write(data)
    classFile.close()
