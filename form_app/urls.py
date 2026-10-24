from django.urls import path
from .views import create_product, product_details, product_search

urlpatterns = [
    path('', create_product, name='create_product'),
    path('create/', create_product, name='create_product_alias'),
    path('products/<int:pk>/', product_details, name='product_details'),
    path('product/<int:pk>/', product_details, name='product_details_alias'),
    path('search/', product_search, name='product_search'),
]
