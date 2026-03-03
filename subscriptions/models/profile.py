from django.db import models
from users.models import User
from subscriptions.models import Plan
from subscriptions.models.storage import Storage as SubscriptionStorage


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    profile_pic = models.FileField(
        upload_to="media/subscriptions/profile_pics",
        null=True,
        blank=True
    )

    background_pic = models.ImageField(
        upload_to="media/subscriptions/background_pics",
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    icd_code = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )

    pr_number = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )

    se_number = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )

    current_plans = models.ManyToManyField(
        Plan,
        blank=True,
        related_name="profiles_current_plans"
    )

    current_storage = models.ManyToManyField(
        SubscriptionStorage,
        blank=True,
        related_name="profiles_current_storage"
    )

    available_storage = models.ManyToManyField(
        SubscriptionStorage,
        blank=True,
        related_name="profiles_available_storage"
    )

    max_storage_gb = models.BigIntegerField(
        default=50,
        help_text="Total quota across all storages"
    )

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.name or f"Profile-{self.pk}"

    # ----------------------
    # Storage Calculations
    # ----------------------

    def total_used_gb(self):
        return sum(s.used_gb for s in self.available_storage.all())

    def total_quota_gb(self):
        return sum(s.quota_gb for s in self.available_storage.all())

    def is_over_platform_limit(self):
        return self.total_used_gb() > self.max_storage_gb

    # ----------------------
    # Storage Operations
    # ----------------------

    def mount(self, storage: SubscriptionStorage):
        """Make a storage volume active."""
        if self.available_storage.filter(pk=storage.pk).exists():
            self.current_storage.add(storage)

    def unmount(self, storage: SubscriptionStorage):
        """Unmount without removing from available pool."""
        self.current_storage.remove(storage)

    def provision_storage(self, storage: SubscriptionStorage):
        """Add a new storage volume to the profile's pool."""
        self.available_storage.add(storage)