from graphene import relay
from graphene_django import DjangoObjectType
from subscriptions.models import Storage
import graphene


class StorageType(DjangoObjectType):
    class Meta:
        model = Storage
        interfaces = (relay.Node, )
        fields = [

        ]