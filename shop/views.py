from django.shortcuts import render
from .models import Product
from django.views.generic import ListView
# Create your views here.

def shop(request):
    product = Product.objects.all()
    return render(request,'shop.html',{'pro':product})