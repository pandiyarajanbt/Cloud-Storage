from graphene_django_cud.mutations import DjangoCreateMutation
from subscriptions.models import StorageNode


class CreateStorageNode(DjangoCreateMutation):
    class Meta:
        model = StorageNode
        input = "create_storage_node"
        fields = [
            "name", "node_id", "node_type", "tier", "status",
            "datacenter", "rack", "ip_address", "mount_path",  "total_capacity_gb", "used_capacity_gb",
            "reserved_capacity_gb", "read_speed_mbps", "write_speed_mbps", "iops", "is_replica",
            "replica_of", "is_active", "created_at", "updated_at", "last_health_check"
        ]
