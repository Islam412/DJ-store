from django.urls import path
from .views import ShopView,detail
from . import views

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('<int:pk>',detail.as_view(),name='detail'),
    path('cart/', views.view_cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    

]
