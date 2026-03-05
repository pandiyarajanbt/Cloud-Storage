import graphene
from graphql import GraphQLError
from users.models import User
import graphql_jwt


class RegisterMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, email, password):
        if User.objects.filter(email=email).exists():
            raise GraphQLError('User already exists')

        user = User.objects.create_user(
            email=email,
            username=email,
            password=password
        )

        return RegisterMutation(success=True)


class UserMutation(graphene.ObjectType):
    register = RegisterMutation.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    refresh = graphql_jwt.Refresh.Field()
