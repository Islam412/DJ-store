from django.shortcuts import render
from django.db.models import Count
from shop.models import Product, Category, CartItem, wishlistItem
from django.contrib.auth import get_user_model

def product_search_view(request):
    # Get the count of cart items for the current user
    cart_items_count = CartItem.objects.filter(cart__user=request.user).count()

    # Get the count of wishlist items for the current user
    WishlistItem = get_user_model()
    wishlist_items_count = wishlistItem.objects.filter(wishlist__user=request.user).count()

    search_query = request.GET.get('search_query')
    category_id = request.GET.get('category', None)

    products = Product.objects.all()
    pro = Product.objects.all()

    if search_query:
        products = products.filter(Name__icontains=search_query)

    if category_id:
        products = products.filter(Category_id=category_id)

    products = products[:4]

    context = {
        'search_query': search_query,
        'products': products,
        'pro': pro,
        'cart_items_count': cart_items_count,
        'wishlist_items_count': wishlist_items_count,
        'categories': Category.objects.annotate(product_count=Count('products')),
    }

    return render(request, 'home/index.html', context)
