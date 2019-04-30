from django.contrib import admin
from .models import Treasur, Deposit, Withdraw

@admin.register(Treasur)
class TreasurAdmin(admin.ModelAdmin):
    pass

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    pass

@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    pass