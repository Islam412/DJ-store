from django.db import models
from account.models import CustomUser
from cart.models import CartItem
from django.utils import timezone
# Create your models here.
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