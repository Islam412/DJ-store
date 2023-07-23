from django.shortcuts import render,redirect
from .models import Product,Cart, CartItem
from django.views.generic import ListView,DeleteView,DetailView

# Create your views here.

class ShopView(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'pro'
    






class detail(DetailView):
    model = Product
    template_name = 'detail.html'
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
    return render(request, 'cart.html', {'cart_items': cart_items})