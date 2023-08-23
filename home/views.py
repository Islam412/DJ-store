from django.shortcuts import render
from django.db.models import Count
from shop.models import Product, Category,Flash,Ofer
from cart.models import CartItem, wishlistItem 
from contact.models import Info
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

def product_search_view(request):
    info = Info.objects.first()
    cart_items_count = 0
    wishlist_items_count = 0
    flash = Flash.objects.all()
    if request.user.is_authenticated:
        cart_items_count = CartItem.objects.filter(cart__user=request.user).count()
        wishlist_items_count = wishlistItem.objects.filter(wishlist__user=request.user).count()

    search_query = request.GET.get('search_query')
    category_id = request.GET.get('category', None)
    ofer = Ofer.objects.all()
    products = Product.objects.all()
    pro = Product.objects.order_by('-id')[:4]
   
    product = Product.objects.all()

    if search_query:
        products = products.filter(Name__icontains=search_query)

    if category_id:
        products = products.filter(Category_id=category_id)

    products = products[:4]

    context = {
        'search_query': search_query,
        'products': products,
        'product':product,
        'flash':flash,
        'pro': pro,
        'cart_items_count': cart_items_count,
        'wishlist_items_count': wishlist_items_count,
        'categories': Category.objects.annotate(product_count=Count('products')),
        'ofer':ofer,
        'info':info,
        
    }

    return render(request, 'home/index.html', context)

