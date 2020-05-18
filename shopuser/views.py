from django.db.models import F
from django.shortcuts import render

from storage.models import StorageProduct
from .models import Customer, Seller
from orders.models import Order, OrderItem
from shop.models import Category, ProductVersion


def user_select(request):
    sellers = Seller.objects.all()
    customers = Customer.objects.all()
    averange = Order.objects.get(id=5).delivery_average_time

    items_with_changed_price = OrderItem.objects.filter(storage_product__prices_story__date__range=[F('main_order__date'), F('main_order__delivery_time')])

    p_versions = ProductVersion.objects.all()
    products_with_more_than_2_sellers = []
    for p_version in p_versions:
        sellers = {st_product.seller for st_product in p_version.storage_products.all()}
        if len(sellers) >= 2:
            products_with_more_than_2_sellers.append(p_version)

    return render(request, 'base.html', {
        'sellers': sellers,
        'customers': customers,
        'averange': averange,
        'items_with_changed_price': items_with_changed_price,
        'products_with_more_than_2_sellers': products_with_more_than_2_sellers
    })


def get_customer(request, user_id):
    user = Customer.objects.get(id=user_id)
    user_orders = user.orders.all() #1
    return render(request, 'customers/customer.html', {'user': user, 'user_orders': user_orders})


def get_seller(request, user_id):
    user = Seller.objects.get(id=user_id)
    sales = OrderItem.objects.filter(storage_product__seller=user).all()
    products = StorageProduct.objects.filter(seller=user)
    my_users = {i.main_order.user for i in sales} #2



    return render(request, 'sellers/seller.html',
                                                {'user': user,
                                                 'sales': sales,
                                                 'my_users': my_users,
                                                 'products': products,
                                                 })







