from graphene import relay
from graphene_django import DjangoObjectType
from subscriptions.models import Profile
import graphene


class ProfileType(DjangoObjectType):
    total_used_gb = graphene.Float()
    total_quota_gb = graphene.Float()
    is_over_platform_limit = graphene.Boolean()

    class Meta:
        model = Profile
        interfaces = (relay.Node,)
        fields = "__all__"

    def resolve_total_used_gb(self, info):
        return self.total_used_gb()

    def resolve_total_quota_gb(self, info):
        return self.total_quota_gb()

    def resolve_is_over_platform_limit(self, info):
        return self.is_over_platform_limit()