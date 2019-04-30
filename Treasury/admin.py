from django.contrib import admin
from .models import Treasur

@admin.register(Treasur)
class TreasurAdmin(admin.ModelAdmin):
    pass