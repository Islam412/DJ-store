from django.shortcuts import render
from shop.models import Product
from shop.views import get_cart_items_count  ,   get_wishlist_items_count 

def product_search_view(request):
    cart_items_count = get_cart_items_count(request.user)
    wishlist_items_count = get_wishlist_items_count(request.user)
    search_query = request.GET.get('search_query')
    products = Product.objects.all()[:4]
    pro = Product.objects.all()[:4]
    if search_query:
        products = products.filter(Name__icontains=search_query)

    context = {
        'search_query': search_query,
        'products': products,
        'pro': pro,
        'cart_items_count':cart_items_count,
        'wishlist_items_count':wishlist_items_count,
    }

    return render(request, 'home/index.html', context)




 # Replace 'your_shop_app' with the actual name of your shop app

