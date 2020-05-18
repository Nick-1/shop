from django.urls import path
from . import views

app_name = 'storage'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:st_product_id>/', views.get_storage_product, name='get_storage_product'),


]
