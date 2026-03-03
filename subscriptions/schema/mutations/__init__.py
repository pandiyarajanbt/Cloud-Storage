from subscriptions.schema.mutations.profile import CreateProfileMutation



import graphene

class SubscriptionMutation(graphene.ObjectType):
    createprofile = CreateProfileMutation.Field()
