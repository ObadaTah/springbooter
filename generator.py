import generateClass, generateController, generateModelAssembler, generateNotFoundAdvice, generateRepository, generateNotFoundException
import os

# classes = [
#     {
#         "className": "Academic",
#         "attr": {
#             "badge": "String",
#             "education": "String",
#             "organizationId": "User",
#             "position": "Position",
#         },
#     },
#     {"className": "Organization", "attr": {"type": "String", "verified": "Boolean"}},
#     {
#         "className": "Post",
#         "attr": {
#             "postId": "Long",
#             "content": "String",
#             "visibility": "Visibility",
#             "publisher": "User",
#             "interactionCount": "Integer",
#             "opinionsCount": "Integer",
#             "reShare": "Post",
#         },
#     },
#     {"className": "Article", "attr": {"content": "String"}},
#     {
#         "className": "ResearchPaper",
#         "attr": {
#             "description": "String",
#             "validatedBy": "Organization",
#             "subject": "String",
#             "language": "String",
#             "noOfPages": "Integer",
#         },
#     },
#     {
#         "className": "Media",
#         "attr": {"mediaId": "Long", "type": "MediaType", "path": "String"},
#     },
#     {
#         "className": "Interaction",
#         "attr": {
#             "interactionId": "Long",
#             "type": "InteractionType",
#             "timestamp": "datetime",
#         },
#     },
#     {"className": "Opinion", "attr": {"opinionId": "Long", "content": "Text"}},
#     {
#         "className": "Notification",
#         "attr": {
#             "notificationId": "Long",
#             "content": "String",
#             "status": "Status",
#             "timestamp": "datetime",
#         },
#     },
# ]

classes = [
    {
        "className": "Journal",
        "attr": {
            "name": "String",
            "description": "String",
            "subject": "String",
            "title": "String",
            "language": "String",
            "publisher": "User",
            "noOfPages": "Integer",
            "validatedBy": "Organization",
            "visibility": "String",
            "contributors": "List<User>",
            "requestForAccess": "List<User>",
        },
    }
]

if not os.path.isdir("src"):
    os.mkdir("src")
for c in classes:

    path = "src/" + c["className"]
    if not os.path.isdir(path):
        os.mkdir(path)
    path += "/" + c["className"]
    packageName = "package " + "edu.bethlehem.scinexus." + c["className"] + ";"
    generateClass.generateClass(path, c["className"], c["attr"], packageName)
    generateController.generateController(path, c["className"], c["attr"], packageName)
    generateModelAssembler.generateModelAssembler(path, c["className"], packageName)
    generateNotFoundAdvice.generateNotFoundAdvice(path, c["className"], packageName)
    generateRepository.generateRepository(path, c["className"], packageName)
    generateNotFoundException.generateNotFoundException(
        path, c["className"], packageName
    )
