from django.shortcuts import render,redirect,get_object_or_404
from django.db import transaction
from shop.models import Product
from .models import CartItem,Cart,Wishlist,wishlistItem


# Create your views here.
def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        product = Product.objects.get(pk=product_id)  # Replace with your product model
        cart_item, created = CartItem.objects.get_or_create(cart=cart, user=request.user, product=product)
        
        # Check if the cart item was created and not already in the cart
        if not created:
            if cart_item.quantity == 0:
                cart_item.quantity = 1
            else:
                cart_item.quantity += 1
            cart_item.save()

    return redirect('cart')





def view_cart(request):
    if request.user.is_authenticated:
        # Filter the cart based on the currently authenticated user
        cart = Cart.objects.filter(user=request.user).first()

        if cart:
            cart_items = CartItem.objects.filter(cart=cart)
        else:
            cart_items = None

        if request.method == 'POST':
            item_id = request.POST.get('item_id')
            new_quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not provided
            cart_item = CartItem.objects.get(id=item_id)

            if new_quantity > 0:
                cart_item.quantity = new_quantity
                cart_item.save()

        # Create a list of numbers from 1 to 10 for the quantity dropdown
        quantity_choices = list(range(1, 11))

        return render(request, 'shop/cart.html', {'cart_items': cart_items, 'quantity_choices': quantity_choices})
    else:
        return render(request, 'shop/cart.html', {'cart_items': None})




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








def calculate_total_price(cart_items):
    total_price = 0
    for cart_item in cart_items:
        total_price += cart_item.product.Price * cart_item.quantity
    return total_price




