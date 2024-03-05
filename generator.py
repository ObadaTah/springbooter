import generateClass, generateController, generateModelAssembler, generateNotFoundAdvice, generateRepository, generateNotFoundException
import os

classes = [
    {
        "className": "Payment",
        "attr": {"amount": "double", "date": "LocalDate", "type": "PaymentType"},
    },
    {
        "className": "Patient",
        "attr": {"name": "String", "date": "LocalDate", "age": "Integer"},
    },
]


if not os.path.isdir("src"):
    os.mkdir("src")
for c in classes:

    path = "src/" + c["className"]
    if not os.path.isdir(path):
        os.mkdir(path)
    path += "/" + c["className"]
    packageName = "package " + "edu.bethlehem.test." + c["className"] + ";"
    generateClass.generateClass(path, c["className"], c["attr"], packageName)
    generateController.generateController(path, c["className"], c["attr"], packageName)
    generateModelAssembler.generateModelAssembler(path, c["className"], packageName)
    generateNotFoundAdvice.generateNotFoundAdvice(path, c["className"], packageName)
    generateRepository.generateRepository(path, c["className"], packageName)
    generateNotFoundException.generateNotFoundException(
        path, c["className"], packageName
    )
