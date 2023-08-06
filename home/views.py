from django.shortcuts import render
from shop.models import Product,Category,SubCategory
from shop.views import get_cart_items_count  ,   get_wishlist_items_count 
from django.db.models import Count

'''
def product_search_view(request):
    search_query = request.GET.get('search_query')
    category_id = request.GET.get('category', None)

    products = Product.objects.all()

    if search_query:
        products = products.filter(Name__icontains=search_query)

    if category_id:
        products = products.filter(Category_id=category_id)

    pro = products[:4]

    context = {
        'search_query': search_query,
        'products': products,
        'pro': pro,
        'categories': Category.objects.annotate(product_count=Count('products')),
    }

    return render(request, 'home/index.html', context)

'''
def product_search_view(request):
    cart_items_count = get_cart_items_count(request.user)
    wishlist_items_count = get_wishlist_items_count(request.user)
    search_query = request.GET.get('search_query')
    category_id = request.GET.get('category', None)  # Get the category_id from the URL query string

    products = Product.objects.all()[:4]
    pro = Product.objects.all()[:4]

    if search_query:
        products = products.filter(Name__icontains=search_query)

    if category_id:
        products = products.filter(Category_id=category_id)

    context = {
        'search_query': search_query,
        'products': products,
        'pro': pro,
        'cart_items_count': cart_items_count,
        'wishlist_items_count': wishlist_items_count,
        'categories':Category.objects.annotate(product_count=Count('products')),
    }

    return render(request, 'home/index.html', context)