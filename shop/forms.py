from django import forms
from .models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Name', 'Price', 'Description', 'Image', 'Availability', 'Color', 'Category', 'SubCategory', 'Brand']
