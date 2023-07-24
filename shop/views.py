from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, redirect
from .models import Product,Cart, CartItem
from django.views.generic import ListView,DeleteView,DetailView
from .models import WishlistItem
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


def delete_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart') 











def add_to_wishlist(request, id):
    item = Product.objects.get(id=id)  # Replace YourShopItemModel with your actual shop item model.
    WishlistItem.objects.create(name=item.Name, Image = item.Image )
    return redirect('wishlist_list')


def wishlistitem_list(request):
    pro = WishlistItem.objects.all()
    return render(request,'wishlist/wishlistitem_list.html',{'pro':pro})



def delete_wishlist_item(request, id):
    WishlistItem.objects.filter(id=id).delete()
    return redirect('wishlist_list')

