from django.db import models


class Supply(models.Model):
    date = models.DateField()

    def __str__(self):
        return f'{self.date}'


class SupplyItem(models.Model):
    count = models.IntegerField()
    supply = models.ForeignKey(Supply, related_name='supply_items', on_delete=models.CASCADE)
    product = models.ForeignKey('shop.ProductVersion', related_name='supply_items', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.main_product.title}'


class StorageProduct(models.Model):
    product = models.ForeignKey('shop.ProductVersion', related_name='storage_products', on_delete=models.CASCADE)
    seller = models.ForeignKey('shopuser.Seller', related_name='storage_products', on_delete=models.CASCADE)
    categories = models.ForeignKey('shop.Category', related_name='storage_products', on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.FloatField()
    availability = models.BooleanField()

    def save(self, *args, **kwargs):
        super(StorageProduct, self).save(*args, **kwargs)
        PricesStory(price=self.price, storage_product=self).save()

    def __str__(self):
        props = self.product.dynamic_properties.all()
        return  f'{self.product.main_product.title} || {props[0]}/{props[1]}/{props[2]}/{props[3]} || Seller: {self.seller.user.username} || price: {self.price} || count: {self.count}'


class PricesStory(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    storage_product = models.ForeignKey('StorageProduct', related_name='prices_story', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date', )

    def __str__(self):
        return f'date: {self.date} :: price: {self.price}'