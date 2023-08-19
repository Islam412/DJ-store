from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, redirect
from .models import Product, Brand , Category,SubCategory,Review,Product_Images
from cart.models import Cart,CartItem,Wishlist,wishlistItem
from django.views.generic import ListView,DeleteView,DetailView
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django import forms
from django.db.models import Count
from .forms import AddProductForm,AddReviewForm
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





def Shop_grid_View(request, category_id=None,sub_id=None):
    sort_by = request.GET.get('sort_by', '')  # Get the sorting parameter from the URL query string
    pro = Product.objects.all()
    subCategory = SubCategory.objects.annotate(product_count=Count('products'))
    if category_id:
        subCategory = subCategory.filter(category_id=category_id)
        pro = pro.filter(Category_id=category_id)
    if sub_id:
        pro = pro.filter(SubCategory = sub_id)

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
    
    # Get the subcategory of the current product
    subcategory = pro.SubCategory
    
    # Fetch related products with the same subcategory
    related = Product.objects.filter(SubCategory=subcategory).exclude(id=pk)
    
    # Fetch images for related products
    related_images = Product_Images.objects.filter(product=pro)
    
    color_code = pro.Color
    color_name = COLOR_MAP.get(color_code, 'Unknown Color')
    
    # Fetch existing reviews for the product
    reviews = Review.objects.filter(product=pro)

    if request.method == 'POST':
        form = AddReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = pro
            form.user = request.user
            form.save()
            # Redirect back to the detail page after adding the review
            return redirect('detail', pk=pk)
    else:
        form = AddReviewForm()

    return render(request, 'shop/detail.html', {
        'pro': pro,
        'color_name': color_name,
        'reviews': reviews,
        'form': form,
        'related': related,
        'related_images': related_images,  # Pass the related product images to the template
    })


@login_required
def add_product(request):
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect('shop')  # Redirect to product list page after adding product
    else:
        form = AddProductForm()

    return render(request, 'shop/add_product.html', {'form': form})



