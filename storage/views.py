from django.shortcuts import render

from storage.models import StorageProduct, PricesStory


def index(request):
    products = StorageProduct.objects.all()
    return render(request, 'storage/all_products.html', {'products': products})


def get_storage_product(request, st_product_id):
    product = StorageProduct.objects.get(id=st_product_id)
    prices_story = PricesStory.objects.filter(storage_product=product)
    return render(request, 'storage/detail.html', {'product': product, 'prices_story': prices_story})