from django.db import models
from django.contrib.auth import get_user_model
from lib.storage_types import StorageType, StorageStatus
from lib.choice import choices_the_options
from subscriptions.models.storage_node import StorageNode

User = get_user_model()

class Storage(models.Model):
    """
    A logical storage allocation assigned to a profile.
    Backed by one or more StorageNodes on your platform.
    """

    # Identity
    label = models.CharField(max_length=255)
    storage_type = models.CharField(max_length=20, choices=choices_the_options(StorageType), default='personal')
    status = models.CharField(max_length=20, choices=choices_the_options(StorageStatus), default='active')

    # Backed by physical nodes
    nodes = models.ManyToManyField(
        StorageNode,
        blank=True,
        related_name='logical_storages',
        help_text="Physical nodes backing this logical storage"
    )

    # Quota (in GB) — set per user/plan
    quota_gb = models.BigIntegerField(default=10)
    used_gb = models.BigIntegerField(default=0)

    # Access
    is_encrypted = models.BooleanField(default=True)
    is_public = models.BooleanField(default=False)
    access_key = models.CharField(max_length=512, blank=True, null=True)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Storage"
        verbose_name_plural = "Storages"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.label} ({self.quota_gb}GB — {self.get_status_display()})"

    @property
    def free_gb(self):
        return self.quota_gb - self.used_gb

    @property
    def usage_percentage(self):
        if self.quota_gb == 0:
            return 0
        return round((self.used_gb / self.quota_gb) * 100, 2)

    @property
    def is_over_quota(self):
        return self.used_gb >= self.quota_gb

