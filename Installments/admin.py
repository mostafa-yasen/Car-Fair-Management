from django.contrib import admin
from .models import Installment

@admin.register(Installment)
class InstallmentAdmin(admin.ModelAdmin):
    pass