from graphene_django_cud.mutations import DjangoCreateMutation
from subscriptions.models import Storage

class CreateStorageMutation(DjangoCreateMutation):
    class Meta:
        model = Storage
        input = "create_storage"
        fields = [
            "label", "storage_type", "status", "node", "quota_gb", "used_gb",
            "is_encrypted", "is_public", "access_key", "created_at", "updated_at",
            "expires_at"
        ]