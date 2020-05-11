from django.contrib import admin
from orders.models import Order, OrderItems


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 1


@admin.register(Order)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInline]