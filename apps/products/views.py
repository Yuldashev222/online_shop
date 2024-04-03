from django.shortcuts import render

from apps.products.models import Product


def product_list(request):
    products = Product.objects.all().order_by('-pk')
    ctx = {
        'products': products
    }
    return render(request, 'products/product_list.html', ctx)

