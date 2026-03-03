from subscriptions.schema.types.profile import ProfileType


import graphene
from graphene_django.fields import DjangoConnectionField


class SubscritionsQuery(graphene.ObjectType):
    profiles = DjangoConnectionField(ProfileType)