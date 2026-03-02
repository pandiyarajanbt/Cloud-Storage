import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.types import Node
from users.models import User
from graphene_django.fields import DjangoConnectionField

class UserType(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (Node, )
        fields = "__all__"


class UserQuery(graphene.ObjectType):
    users = DjangoConnectionField(UserType)