import graphene

# User
from users.schema.mutation import UserMutation

class Query(graphene.ObjectType):
    ping = graphene.String()

    def resolve_ping(root, info):
        return "pong"


class Mutation(UserMutation, graphene.ObjectType):
    pass



schema = graphene.Schema(query=Query, mutation=Mutation)