from django.contrib import admin
from subscriptions.models import(
    Plan, Profile, StorageNode, Storage
)

admin.site.register(Profile)
admin.site.register(Plan)
admin.site.register(StorageNode)
admin.site.register(Storage)