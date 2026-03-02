from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models.user_manager import UserManager


class User(AbstractUser):
    objects = UserManager()

    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'