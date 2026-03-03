import graphene
from graphene_django_cud.mutations import DjangoCreateMutation, DjangoUpdateMutation
from subscriptions.models import Profile
from subscriptions.schema.types.profile import ProfileType  # noqa: F401  (ensures model type is registered)

class CreateProfileMutation(DjangoCreateMutation):
    class Meta:
        model = Profile
        input = "CreateProfileinput"
        fields = [
            "user", "profile_pic", "background_pic", "name", "icd_code"
            , "pr_number", "se_number", "current_plans", "current_storage", "available_storage",
            "max_storage_gb", "timestamp"
        ]