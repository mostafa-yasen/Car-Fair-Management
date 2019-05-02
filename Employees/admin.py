from django.contrib import admin
from .models import Manager, Employee

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass