from graphene_django.views import GraphQLView

class CustomGraphQLView(GraphQLView):
    graphiql_template = "graphiql_old.html"