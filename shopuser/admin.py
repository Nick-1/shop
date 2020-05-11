from django.contrib import admin
from .models import Seller, Customer, Address


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1


@admin.register(Customer)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('user', )
    inlines = [AddressInline]


@admin.register(Seller)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('user', )
