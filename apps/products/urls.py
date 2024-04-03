from django.urls import path

from apps.products.views import product_list

urlpatterns = [
    path('products/', product_list, name='product-list')
]