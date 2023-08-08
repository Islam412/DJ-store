from django.contrib import admin
from . models import Product,Cart,Wishlist , Order , Category , SubCategory , Brand,Review
# Register your models here.

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(Review)
