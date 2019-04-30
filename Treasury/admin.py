from django.contrib import admin
from .models import Treasur, Deposit

@admin.register(Treasur)
class TreasurAdmin(admin.ModelAdmin):
    pass

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    pass