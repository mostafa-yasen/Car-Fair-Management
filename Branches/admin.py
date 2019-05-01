from django.contrib import admin
from .models import Branch, Notification

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    pass

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass