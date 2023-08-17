from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.conf import settings
import json
from django.utils import timezone
from account.models import CustomUser
#_________________________________________
class Category(models.Model):
    image = models.ImageField(upload_to='category/',null=True,blank=True)
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
class Product_Images (models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,related_name='Product_images',null=True,blank=True)
    image1=models.ImageField(upload_to='productimages/',null=True,blank=True)
    image2=models.ImageField(upload_to='productimages/',null=True,blank=True)
    image3=models.ImageField(upload_to='productimages/',null=True,blank=True)
    image4=models.ImageField(upload_to='productimages/',null=True,blank=True)
    image5=models.ImageField(upload_to='productimages/',null=True,blank=True)
#_________________________________________________________

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
class Ofer(models.Model):
    price = models.IntegerField()
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,related_name='ofer_product',null=True,blank=True)
    def __str__(self):
        return str(self.product)