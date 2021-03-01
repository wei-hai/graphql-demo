import graphene

class ExceptionInfoField(graphene.ObjectType):
    message = graphene.String()
