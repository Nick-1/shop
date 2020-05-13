from django.contrib import admin
from orders.models import Order, OrderItem


class OrderItemsInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInline]