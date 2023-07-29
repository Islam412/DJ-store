from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.conf import settings
import json
from account.models import CustomUser
# Create your models here.


class Product(models.Model):


    choise=[
    ('Laptop','Laptop'),
    ('Computer','Computer'),
    ('Phone','Phone'),
    ('Screen','Screen'),
    ]


    Name = models.CharField(max_length=60)
    Price = models.FloatField()
    Description = models.TextField(max_length=2000)
    Image = models.ImageField(upload_to='images/')
    Availability = models.BooleanField(default=True)
    Color=ColorField(default='#000000')
    Categore = models.CharField(max_length=50, choices=choise, blank=True, null=True)
    Brand = models.CharField(max_length=20,null=True)




    def __str__(self):
        return self.Name
    



class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"


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
    cart_items = models.JSONField(default=list)  # Set a default value of an empty list

    # Add any other fields you need for the order

    def save_cart_items(self, cart_items):
        self.cart_items = json.dumps([{
            'product_name': item.product.Name,
            'quantity': item.quantity,
            'price': item.product.Price
        } for item in cart_items])

    def __str__(self):
        return self.cart_items



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
