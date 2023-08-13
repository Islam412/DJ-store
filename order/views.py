from django.shortcuts import render,redirect
from cart.models import Cart,CartItem
from .models import Order
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django import forms
from django.db.models import Count


# Create your views here.

def order_confirmation(request):
    return render(request, 'shop/confirm.html')

def calculate_total_price(cart_items):
    total_price = 0
    for cart_item in cart_items:
        total_price += cart_item.product.Price * cart_item.quantity
    return total_price



def checkout(request):
    if request.user.is_authenticated:
        # Filter the cart based on the currently authenticated user
        cart = Cart.objects.get(user=request.user)

        if cart:
            cart_items = CartItem.objects.filter(cart=cart)
            total_price =calculate_total_price(cart_items)
        else:
            cart_items = None
            total_price = 0

        if request.method == 'POST':
            name = request.POST.get('name')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

            with transaction.atomic():
                order = Order.objects.create(
                    user=request.user,
                    name=name,
                    address=address,
                    phone=phone,
                    email=email,
                    total_price=total_price
                )

                for cart_item in cart_items:
                    new_quantity = int(request.POST.get(f'quantity_{cart_item.id}', 1))
                    if new_quantity > 0:
                        cart_item.quantity = new_quantity
                        cart_item.save()
                        order.cart_items.add(cart_item)  # Associate cart item with the order

                return redirect('confirm')

    else:
        cart_items = None
        total_price = 0

    return render(request, 'shop/checkout.html', {'cart_items': cart_items, 'total_price': total_price})
