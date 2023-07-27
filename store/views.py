from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.urls import resolve

from store.models import Product, Color, Stock, Category


def index(request):
    current_url_name = resolve(request.path).url_name
    context = {
        'current_url_name': current_url_name
    }
    return render(request, 'store/index.html', context)


def boutique(request):
    current_url_name = resolve(request.path).url_name
    products = Product.objects.prefetch_related('productimage_set').all()
    categorys = Category.objects.all()
    colors = Color.objects.all()

    if request.method == 'GET':

        name = request.GET.get('recherche')
        if name is not None:
            products = products.filter(name__icontains=name)

        category = request.GET.get('category')
        if category is not None:
            products = products.filter(category__name=category)


    paginate_by = 9
    paginator = Paginator(products, paginate_by)

    page_number = request.GET.get('page')
    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:

        products = paginator.page(paginator.num_pages)


    context = {
        'current_url_name': current_url_name,
        'products': products,
        'categorys': categorys,
        'colors': colors
    }
    return render(request, 'store/boutique.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    colors = Color.objects.filter(stock__product=product).distinct()

    color_and_sizes = {}
    for color in colors:
        sizes = Stock.objects.filter(product=product, color=color).values_list('size', flat=True)
        color_and_sizes[color.colorHexadecimal] = list(sizes)

    current_url_name = resolve(request.path).url_name

    context = {
        'current_url_name': current_url_name,
        'product': product,
        'color_and_sizes': color_and_sizes,
    }

    return render(request, 'store/product.html', context)
