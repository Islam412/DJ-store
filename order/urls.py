from django.urls import path
from . import views
urlpatterns=[
    path('',views.checkout, name='checkout'),
    path('confirm/',views.order_confirmation,name='confirm'),
]