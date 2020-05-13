from django.db import models
from shop.models import ProductVersion


class Order(models.Model):
    user = models.ForeignKey('shopuser.Customer', related_name='orders', on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'sum: {self.get_total()}'

    def get_total(self):
        total = 0
        for item in self.items.all():
            total += item.item_sum()
        return total


class OrderItem(models.Model):
    main_order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    storage_product = models.ForeignKey('storage.StorageProduct', on_delete=models.CASCADE, related_name='order_items')

    def item_sum(self):
        return self.count * self.storage_product.price

    def save(self, *args, **kwargs):
        super(OrderItem, self).save(*args, **kwargs)
        self.storage_product.count -= self.count
        if self.storage_product.count <= 0:
            self.storage_product.availability = False
        self.storage_product.save()


class Sale(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    buyer = models.OneToOneField('shopuser.Customer', related_name='purchases', on_delete=models.CASCADE)


class SaleItem(models.Model):
    main_sale = models.ForeignKey(Sale, related_name='sale_items', on_delete=models.CASCADE)
    product = models.ForeignKey('shop.ProductVersion', related_name='sales', on_delete=models.CASCADE)
    count = models.IntegerField(default=1)