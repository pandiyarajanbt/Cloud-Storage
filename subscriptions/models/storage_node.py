from django.db import models
from lib.storage_types import StorageNodeType, StorageNodeStatus, StorageNodeTier
from lib.choice import choices_the_options


# Physical or virtual storage server on your platform
class StorageNode(models.Model):
    # Identity
    name = models.CharField(max_length=255, unique=True)
    node_id = models.CharField(max_length=100, unique=True, help_text="Internal node identifier")
    node_type = models.CharField(max_length=20, choices=choices_the_options(StorageNodeType), default='hdd')
    tier = models.CharField(max_length=10, choices=choices_the_options(StorageNodeTier), default='hot')
    status = models.CharField(max_length=20, choices=choices_the_options(StorageNodeStatus), default='online')

    # Physical location
    datacenter = models.CharField(max_length=100, blank=True, null=True)
    rack = models.CharField(max_length=50, blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    mount_path = models.CharField(max_length=500, blank=True, null=True, help_text="e.g. /mnt/storage/node01")

    # Capacity (in GB)
    total_capacity_gb = models.BigIntegerField(default=0)
    used_capacity_gb = models.BigIntegerField(default=0)
    reserved_capacity_gb = models.BigIntegerField(default=0, help_text="Reserved for system use")

    # Performance
    read_speed_mbps = models.IntegerField(blank=True, null=True)
    write_speed_mbps = models.IntegerField(blank=True, null=True)
    iops = models.IntegerField(blank=True, null=True)

    # Replication
    is_replica = models.BooleanField(default=False)
    replica_of = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='replicas'
    )

    # Metadata
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_health_check = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Storage Node"
        verbose_name_plural = "Storage Nodes"
        ordering = ['datacenter', 'name']

    def __str__(self):
        return f"[{self.node_id}] {self.name} — {self.get_status_display()}"

    # ── Capacity helpers ──────────────────────────────────────────
    @property
    def free_capacity_gb(self):
        return self.total_capacity_gb - self.used_capacity_gb - self.reserved_capacity_gb

    @property
    def usage_percentage(self):
        if self.total_capacity_gb == 0:
            return 0
        return round((self.used_capacity_gb / self.total_capacity_gb) * 100, 2)

    @property
    def is_full(self):
        return self.free_capacity_gb <= 0

    @property
    def is_healthy(self):
        return self.status in ('online',)

    def allocate(self, size_gb: int) -> bool:
        """Try to allocate space. Returns True if successful."""
        if self.free_capacity_gb >= size_gb and self.is_healthy:
            self.used_capacity_gb += size_gb
            self.save(update_fields=['used_capacity_gb'])
            return True
        return False

    def release(self, size_gb: int):
        """Release allocated space back to the node."""
        self.used_capacity_gb = max(0, self.used_capacity_gb - size_gb)
        self.save(update_fields=['used_capacity_gb'])
