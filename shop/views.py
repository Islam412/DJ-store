from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, redirect
from .models import Product,Cart, CartItem , Wishlist , wishlistItem  ,  Order, OrderItem
from django.views.generic import ListView,DeleteView,DetailView
from django.contrib.auth.decorators import login_required
from django.db import transaction
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

        # Check if 'cart' key exists in the session, initialize it with an empty dictionary if not
        if 'cart' not in request.session:
            request.session['cart'] = {}

        product = Product.objects.get(pk=product_id)

        # Get the product name and quantity from the cart session if it exists
        cart_product_info = request.session['cart'].get(str(product_id))

        if cart_product_info:
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            cart_item.quantity += 1
            cart_item.save()

            # Increment the quantity in the cart session
            cart_product_info[1] += 1
        else:
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            cart_product_info = (product.Name, 1)

        # Update the cart session with the product name and quantity
        request.session['cart'][str(product_id)] = cart_product_info

    return redirect('cart')
'''

def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        product = Product.objects.get(pk=product_id)  # Replace with your product model
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    return redirect('cart')

'''

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


def checkout(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        cart = request.session.get('cart', {})

        # Wrap the checkout process in a transaction
        with transaction.atomic():
            order = Order(name=name, phone=phone, address=address, email=email)
            order.save()  # Save the 'Order' instance to get a primary key value

            # Create a list to store OrderItem instances to save later
            order_items_to_save = []

            for product_id, quantity in cart.items():
                product = Product.objects.get(pk=product_id)
                order_item = OrderItem(order=order, product=product, quantity=quantity, price=product.Price)
                order_items_to_save.append(order_item)

            # Save all the OrderItem instances in a single batch
            OrderItem.objects.bulk_create(order_items_to_save)

            # Update the total price of the order based on the calculated value
            order.total_price = order.calculate_total_price()
            order.save()

            request.session['cart'] = {}  # Clear the cart after checkout

        return redirect('order_detail', order_id=order.pk)  # Use 'pk' to access the primary key value

    return render(request, 'shop/checkout.html')