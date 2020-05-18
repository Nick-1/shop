from collections import Counter

from django.shortcuts import render

from shop.models import Category
from storage.models import StorageProduct


def index(request):
    categories = Category.objects.all()
    return render(request, 'categories/index.html', {'categories': categories})


def category_info(request, category_id):
    category = Category.objects.get(id=category_id)
    st_products = StorageProduct.objects.filter(categories=category)
    users_in_category = set()
    all_category_users = []

    for product in st_products:
        for item in product.order_items.all():
            users_in_category.add(item.main_order.user) #3
            all_category_users.append(item.main_order.user)

    counter_orders = Counter(all_category_users)
    more_than_3 = {}

    for key in counter_orders:
        if counter_orders[key] >= 3:
            more_than_3[key] = counter_orders[key] #4

    return render(request, 'categories/detail.html', {
                                                    'category': category,
                                                    'users_in_category': users_in_category,
                                                    'more_than_3': more_than_3})

