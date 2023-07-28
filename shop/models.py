from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.conf import settings
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
    

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    Phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"



class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.name}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.Name} in Cart for {self.cart.user.name}"

    






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
