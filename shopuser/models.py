from django.db import models
from django.conf import settings
from shop.models import ProductVersion
from storage.models import StorageProduct


class Seller(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/user/photo', blank=True)

    def __str__(self):
        return f'user: {self.user.username}'


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/user/photo', blank=True)
    
    def __str__(self):
        return f'user: {self.user.username}'


class Address(models.Model):
    street = models.CharField(max_length=160)
    house = models.CharField(max_length=160)
    flat = models.CharField(max_length=160)
    profile = models.ForeignKey(Customer, related_name='addresses', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile.user.username} || улица: {self.street} || дом: {self.house} || кв.: {self.flat}'