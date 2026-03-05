from subscriptions.schema.types.profile import ProfileType
from subscriptions.schema.types.storage import StorageType
from subscriptions.schema.types.storage_node import StorageNodeTypes

import graphene
from graphene_django.fields import DjangoConnectionField


class SubscritionsQuery(graphene.ObjectType):
    profiles = DjangoConnectionField(ProfileType)
    storage_nodes = DjangoConnectionField(StorageNodeTypes)
    storage = DjangoConnectionField(StorageType)