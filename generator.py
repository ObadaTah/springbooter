import generateClass, generateController, generateModelAssembler, generateNotFoundAdvice, generateRepository, generateNotFoundException
import os

classes = [
    {
        "className": "Payment",
        "attr": {"name": "String", "date": "LocalDate", "type": "PaymentType"},
    },
    {
        "className": "PaymentType",
        "attr": {"name": "String", "description": "String"},
    },
    {
        "className": "User",
        "attr": {"name": "String", "email": "String", "password": "String"},
    },
    {
        "className": "Product",
        "attr": {
            "name": "String",
            "description": "String",
            "price": "Double",
            "quantity": "Integer",
        },
    },
    {
        "className": "Order",
        "attr": {"date": "LocalDate", "total": "Double", "status": "OrderStatus"},
    },
    {
        "className": "OrderStatus",
        "attr": {"name": "String", "description": "String"},
    },
    {
        "className": "OrderItem",
        "attr": {"quantity": "Integer", "price": "Double", "product": "Product"},
    },
]


if not os.path.isdir("src"):
    os.mkdir("src")
for c in classes:

    path = "src/" + c["className"]
    if not os.path.isdir(path):
        os.mkdir(path)
    path += "/" + c["className"]
    generateClass.generateClass(path, c["className"], c["attr"])
    generateController.generateController(path, c["className"], c["attr"])
    generateModelAssembler.generateModelAssembler(path, c["className"])
    generateNotFoundAdvice.generateNotFoundAdvice(path, c["className"])
    generateRepository.generateRepository(path, c["className"])
    generateNotFoundException.generateNotFoundException(path, c["className"])
