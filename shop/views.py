from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, redirect
from .models import Product,Cart, CartItem , Wishlist , wishlistItem   , Order , Brand , Category
from django.views.generic import ListView,DeleteView,DetailView
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django import forms
from django.db.models import Count
# Create your views here.


def ShopView(request, category_id=None):
    pro = Product.objects.all()
    brand = Brand.objects.all()
    category = Category.objects.annotate(product_count=Count('products'))

    if category_id:
        pro = pro.filter(Category_id=category_id)

    return render(request, 'shop/shop.html', {'pro': pro, 'brand': brand, 'category': category})





def Shop_grid_View(request):
    pro = Product.objects.all()
    brand = Brand.objects.all()
    category = Category.objects.all()
    return render(request,'shop/grid.html',{'pro':pro,'brand':brand,'category':category})



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
            # احصل على معلومات التوصيل من النموذج
            name = request.POST.get('name')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

            # أنشئ كائن الطلب (Order) واربطه بالمستخدم
            order = Order.objects.create(
                user=request.user,
                name=name,
                address=address,
                phone=phone,
                email=email,
                total_price=total_price
            )

            # قم بحفظ عناصر سلة التسوق في الطلب
            order.save_cart_items(cart_items)

            # قم بتفريغ سلة التسوق بعد تأكيد الطلب
            cart_items.delete()

            return redirect('confirm/')  # قم بتوجيه المستخدم إلى صفحة شكرًا أو تأكيد الطلب

    else:
        cart_items = None
        total_price = 0

    return render(request, 'shop/checkout.html', {'cart_items': cart_items, 'total_price': total_price})