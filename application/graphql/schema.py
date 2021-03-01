import graphene
from application.graphql.query import Query

schema = graphene.Schema(query=Query)
