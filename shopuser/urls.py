from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('', views.user_select, name='user_select'),
    path('sellers/<int:user_id>/', views.get_seller, name='get_seller'),
    path('customers/<int:user_id>/', views.get_customer, name='get_customer'),

]
