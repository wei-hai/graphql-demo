import graphene
from application.graphql.schemas.organization.query import OrganizationQuery


class Query(OrganizationQuery, graphene.ObjectType):
    hello = graphene.String(name=graphene.String("abc"))

    def resolve_hello(self, info, name):
        print(info)
        return "hello " + name
