from django.shortcuts import render
from shop.models import Product

def product_search_view(request):
    search_query = request.GET.get('search_query')
    products = Product.objects.all()
    pro = Product.objects.all()[1:5]
    if search_query:
        products = products.filter(Name__icontains=search_query)

    context = {
        'search_query': search_query,
        'products': products,
        'pro': pro,
    }

    return render(request, 'home/index.html', context)
