from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.conf import settings
import json
from account.models import CustomUser
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='category', null=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Product(models.Model):


    


    Name = models.CharField(max_length=60)
    Price = models.FloatField()
    Description = models.TextField(max_length=2000)
    Image = models.ImageField(upload_to='images/')
    Availability = models.BooleanField(default=True)
    Color=ColorField(default='#000000')
    Category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products",null=True)
    Brand = models.CharField(max_length=20,null=True)




    def __str__(self):
        return self.Name
    



class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.name}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.Name} in Cart for {self.cart}"


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    cart_items = models.ManyToManyField(CartItem)  # استخدم ManyToManyField لتخزين عناصر سلة التسوق

    # قم بإضافة أية حقول أخرى تحتاجها للطلب

    def __str__(self):
        return f"الطلب رقم {self.pk} للسيد {self.name}"

    def save_cart_items(self, cart_items):
        self.cart_items.set(cart_items)



class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"wishlist for {self.user.name}"

class wishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.Name} in wishlist for {self.wishlist.user.name}"
