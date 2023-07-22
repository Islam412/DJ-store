from django.shortcuts import render
from .models import Product
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