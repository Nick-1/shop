from django.urls import path
from . import views

app_name = 'categorise'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:category_id>/', views.category_info, name='category_info'),
]
