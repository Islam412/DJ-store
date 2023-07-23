from django.shortcuts import render
from shop.models import Product

def product_search_view(request):
    search_query = request.GET.get('search_query')
    products = Product.objects.all()

    if search_query:
        products = products.filter(Name__icontains=search_query)

    return render(request, 'home/index.html', {'search_query': search_query, 'products': products})







