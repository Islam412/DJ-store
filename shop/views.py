from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, redirect
from .models import Product,Cart, CartItem , Wishlist , wishlistItem , Order
from django.views.generic import ListView,DeleteView,DetailView
from django import forms
# Create your views here.

class ShopView(ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'pro'
    






class detail(DetailView):
    model = Product
    template_name = 'shop/detail.html'
    context_object_name = 'pro'







def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        product = Product.objects.get(pk=product_id)  # Replace with your product model
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    return redirect('cart')



def view_cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_items = CartItem.objects.filter(cart=cart)
        else:
            cart_items = None
    else:
        cart_items = None
    return render(request, 'shop/cart.html', {'cart_items': cart_items})


def delete_cart_item(request, id):
    cart_item = get_object_or_404(CartItem, id=id)
    cart_item.delete()
    return redirect('cart') 



def add_to_wishlist(request, product_id):
    if request.user.is_authenticated:
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        product = Product.objects.get(pk=product_id)  # Replace with your product model
        wishlist_Item, created = wishlistItem.objects.get_or_create(wishlist=wishlist, product=product)
        if not created:
            wishlist_Item.quantity += 1
            wishlist_Item.save()
    return redirect('wishlist_list')


def view_wishlist(request):
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user=request.user).first()
        if wishlist:
            wishlist_items = wishlistItem.objects.filter(wishlist=wishlist)
        else:
            wishlist_items = None
    else:
        wishlist_items = None
    return render(request, 'wishlist/wishlistitem_list.html', {'wishlist_items': wishlist_items})


def delete_wishlist_item(request, product_id):
    wishlist_items = get_object_or_404(wishlistItem, id=product_id)
    wishlist_items.delete()
    return redirect('wishlist_list') 




def checkout_view(request):
    user = request.user
    cart = Cart.objects.filter(user=user).first()
    
    if cart:
        cart_items = CartItem.objects.filter(cart=cart)
        total_price = sum(item.product.Price * item.quantity for item in cart_items)
    else:
        cart_items = []
        total_price = 0.00

    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        # Additional check to ensure customer_name is provided
        if not customer_name:
            return render(request, 'shop/checkout.html', {
                'cart_items': cart_items,
                'total_price': total_price,
                'error_message': 'Please provide the customer name.',
            })

        order = Order.objects.create(customer_name=customer_name, email=email, address=address, Phone=phone)
        order.save()
        return redirect('confirm/')  # Replace 'confirm/' with the correct URL path
    else:
        form = None

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'form': form,
    }

    return render(request, 'shop/checkout.html', context)



def get_cart_items_count(user):
    if user.is_authenticated:
        return CartItem.objects.filter(cart__user=user).count()
    return 0


def get_wishlist_items_count(user):
    if user.is_authenticated:
        return wishlistItem.objects.filter(wishlist__user=user).count()
    return 0






def order_confirmation(request):
    return render(request, 'shop/confirm.html')