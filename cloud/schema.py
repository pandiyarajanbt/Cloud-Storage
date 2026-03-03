import graphene

# User
from users.schema.mutation import UserMutation
from users.schema.types import UserQuery

# Subscription
from subscriptions.schema.mutations import SubscriptionMutation
from subscriptions.schema.types import SubscritionsQuery

class Query(UserQuery, SubscritionsQuery, graphene.ObjectType):
    pass

class Mutation(UserMutation, SubscriptionMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)