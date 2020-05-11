from django.contrib import admin
from .models import Supply, SupplyItem, StorageProduct


class SupplyItemInline(admin.TabularInline):
    model = SupplyItem
    extra = 1


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    inlines = [SupplyItemInline]


@admin.register(StorageProduct)
class SupplyAdmin(admin.ModelAdmin):
    pass