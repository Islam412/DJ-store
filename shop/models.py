from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.conf import settings
import json
from django.utils import timezone
from account.models import CustomUser
#_________________________________________
class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name
#____________________________________________________
class SubCategory(models.Model):
    name= models.CharField(max_length=50, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
#________________________________________________________
class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo/',null=True)
    def __str__(self):
        return self.name
#_____________________________________________________
class Product(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='Product_user',null=True,blank=True)
    Name = models.CharField(max_length=60)
    Price = models.FloatField()
    Description = models.TextField(max_length=2000)
    Image = models.ImageField(upload_to='images/')
    Availability = models.BooleanField(default=True)
    Color=ColorField(default='#000000')
    Category=models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="products",null=True)
    SubCategory=models.ForeignKey(SubCategory, on_delete=models.SET_NULL, related_name="products",null=True)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="Brand_Product",null=True)
    def __str__(self):
        return self.Name
#________________________________________________________
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Cart for {self.user.name}"
#________________________________________________________
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.quantity} x {self.product.Name} in Cart for {self.cart}"
#_____________________________________________________________________
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='orders')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    cart_items = models.ManyToManyField(CartItem) 
    created_at = models.DateField(default=timezone.now)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending',null=True) 
    def __str__(self):
        return f"الطلب رقم {self.pk} للسيد {self.name}"
    def save_cart_items(self, cart_items):
        self.cart_items.set(cart_items)
#______________________________________________________________________
class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"wishlist for {self.user.name}"
#_____________________________________________________________________________
class wishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.quantity} x {self.product.Name} in wishlist for {self.wishlist.user.name}"
#___________________________________________________________________________________________

class Review(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,related_name='review_user',null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,related_name='review_product',null=True,blank=True)
    content = models.TextField(max_length=20000)
    date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.content
#__________________________________________________________________________________
class Flash(models.Model):
    pro = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='Flash_product')
    def __str__(self):
        return str(self.pro)
#_____________________________________________________________________________
