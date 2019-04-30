from django.contrib import admin
from .models import Installment, MonthlyInstallment

@admin.register(Installment)
class InstallmentAdmin(admin.ModelAdmin):
    pass

@admin.register(MonthlyInstallment)
class MonthlyInstallmentAdmin(admin.ModelAdmin):
    pass