from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, redirect
from .models import Product,Cart, CartItem , Wishlist , wishlistItem   , Order , Brand , Category,SubCategory
from django.views.generic import ListView,DeleteView,DetailView
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django import forms
from django.db.models import Count
# Create your views here.


def ShopView(request, category_id=None):
    sort_by = request.GET.get('sort_by', '')  # Get the sorting parameter from the URL query string
    pro = Product.objects.all()
    category = Category.objects.annotate(product_count=Count('products'))

    if category_id:
        pro = pro.filter(Category_id=category_id)

    if sort_by == 'price_high':
        pro = pro.order_by('-Price')  # Sorting by price high to low
    elif sort_by == 'price_low':
        pro = pro.order_by('Price')   # Sorting by price low to high

    return render(request, 'shop/shop.html', {'pro': pro, 'category': category})





def Shop_grid_View(request, category_id=None):
    sort_by = request.GET.get('sort_by', '')  # Get the sorting parameter from the URL query string
    pro = Product.objects.all()
    subCategory = SubCategory.objects.annotate(product_count=Count('products'))
    if category_id:
        pro = pro.filter(Category_id=category_id)
        subCategory = subCategory.filter(category_id=category_id)

    if sort_by == 'price_high':
        pro = pro.order_by('-Price')  # Sorting by price high to low
    elif sort_by == 'price_low':
        pro = pro.order_by('Price')   # Sorting by price low to high

    return render(request, 'shop/grid.html', {'pro': pro,'subCategory':subCategory})




COLOR_MAP = {
    '#000000': 'Black',
    '#FFFFFF': 'White',
    '#FF0000': 'Red',
    '#00FF00': 'Green',
    '#0000FF': 'Blue',
    '#FFFF00': 'Yellow',
    '#FF00FF': 'Magenta',
    '#00FFFF': 'Cyan',
    '#800000': 'Maroon',
    '#008000': 'Olive',
    '#000080': 'Navy',
    '#808000': 'Purple',
    '#800080': 'Purple',
    '#008080': 'Teal',
    '#808080': 'Gray',
    '#C0C0C0': 'Silver',
    '#FFC0CB': 'Pink',
    '#FFA500': 'Orange',
    # Add more color mappings here
}

def detail(request, pk):
    pro = Product.objects.get(id=pk)

    color_code = pro.Color
    color_name = COLOR_MAP.get(color_code, 'Unknown Color')

    return render(request, 'shop/detail.html', {'pro': pro, 'color_name': color_name})


def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        product = Product.objects.get(pk=product_id)  # Replace with your product model
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        
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






def order_confirmation(request):
    return render(request, 'shop/confirm.html')



def calculate_total_price(cart_items):
    total_price = 0
    for cart_item in cart_items:
        total_price += cart_item.product.Price * cart_item.quantity
    return total_price



def checkout(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_items = CartItem.objects.filter(cart=cart)
            total_price = calculate_total_price(cart_items)
        else:
            cart_items = None
            total_price = 0

        if request.method == 'POST':
            name = request.POST.get('name')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

            order = Order.objects.create(
                user=request.user,
                name=name,
                address=address,
                phone=phone,
                email=email,
                total_price=total_price
            )

            for item in cart_items:
                new_quantity = int(request.POST.get(f'quantity_{item.id}', 1))
                if new_quantity > 0:
                    cart_item = CartItem.objects.get(id=item.id)
                    cart_item.quantity = new_quantity
                    cart_item.save()
                    order.cart_items.add(cart_item)

            cart_items.delete()
            return redirect('confirm/')

    else:
        cart_items = None
        total_price = 0

    return render(request, 'shop/checkout.html', {'cart_items': cart_items, 'total_price': total_price})
