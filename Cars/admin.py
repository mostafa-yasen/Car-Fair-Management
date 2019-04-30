from django.contrib import admin
from .models import Car, Expense

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass