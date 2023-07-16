from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import resolve

from store.models import Product


def index(request):
    current_url_name = resolve(request.path).url_name
    context = {
        'current_url_name': current_url_name
    }
    return render(request ,'store/index.html' ,context)


def boutique(request):
    current_url_name = resolve(request.path).url_name
    products = Product.objects.all()
    context = {
        'current_url_name': current_url_name,
        'products': products
    }
    return render(request ,'store/boutique.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    current_url_name = resolve(request.path).url_name
    context = {
        'current_url_name': current_url_name,
        'product': product
    }
    return render(request ,'store/product.html' , context)

