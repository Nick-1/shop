from django.db import models


class Office(models.Model):
    seller = models.OneToOneField('shopuser.Seller', related_name='office', on_delete=models.CASCADE)


class OfficeItemProduct(models.Model):
    office = models.ForeignKey(Office, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('shop.ProductVersion', related_name='item_products', on_delete=models.CASCADE)
    count = models.IntegerField(default=0)


