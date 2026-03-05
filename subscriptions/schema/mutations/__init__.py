from subscriptions.schema.mutations.profile import CreateProfileMutation
from subscriptions.schema.mutations.storage import CreateStorageMutation
from subscriptions.schema.mutations.storage_node import CreateStorageNode



import graphene

class SubscriptionMutation(graphene.ObjectType):
    createprofile = CreateProfileMutation.Field()
    createstorage = CreateStorageMutation.Field()
    createstoragenode = CreateStorageNode.Field()
