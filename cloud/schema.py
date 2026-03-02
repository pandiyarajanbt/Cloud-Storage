import graphene

# User
from users.schema.mutation import UserMutation
from users.schema.types import UserQuery

class Query(UserQuery, graphene.ObjectType):
    pass

class Mutation(UserMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)