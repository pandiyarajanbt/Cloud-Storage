from graphene import relay
from graphene_django import DjangoObjectType
from subscriptions.models import StorageNode


class StorageNodeTypes(DjangoObjectType):
    class Meta:
        model = StorageNode
        interfaces = (relay.Node, )
        fields = '__all__'