from django import forms
from .models import Product,Review

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Name', 'Price', 'Description', 'Image', 'Availability', 'Color', 'Category', 'SubCategory', 'Brand']




class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']