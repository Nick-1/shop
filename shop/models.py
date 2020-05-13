from django.db import models
from django.db.models import Sum

from storage.models import SupplyItem


class Section(models.Model):
    title = models.CharField(max_length=100)
    sellers = models.ForeignKey('shopuser.Seller', on_delete=models.CASCADE, related_name='sections', blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.title


class DynamicProperty(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='dynamic_properties', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class DynamicPropertyValue(models.Model):
    dynamic_property = models.ForeignKey(DynamicProperty, related_name='values', on_delete=models.CASCADE)
    value = models.CharField(max_length=60)
    productVersion = models.ForeignKey('ProductVersion', related_name='dynamic_properties', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.value}'


class Brand(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brands/images', blank=True, null=True,)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    categories = models.ManyToManyField(Category, related_name='products')
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class ProductImage(models.Model):
    img = models.ImageField(upload_to='products/images', blank=True)
    description = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', null=True, blank=True)

    def __str__(self):
        return self.description


class ProductVersion(models.Model):
    main_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions')

    def __str__(self):
        props = self.dynamic_properties.all()
        return f'{self.main_product.title} || {props[0]}/{props[1]}/{props[2]}/{props[3]}'


class ProductReviews(models.Model):
    pass

