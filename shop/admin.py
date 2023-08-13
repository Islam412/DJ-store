from django.contrib import admin
from . models import Product,Category , SubCategory , Brand,Review , Flash
# Register your models here.

admin.site.register(Product)
#admin.site.register(Order)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(Flash)