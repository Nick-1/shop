from django.contrib import admin
from .models import Office, OfficeItemProduct


class OfficeItemProductInline(admin.TabularInline):
    model = OfficeItemProduct
    extra = 1


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    inlines = [OfficeItemProductInline]