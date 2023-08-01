from django.urls import path
from .views import ShopView,detail ,  Shop_grid_View
from . import views

urlpatterns = [
    path('', ShopView, name='shop'),
    path('grid', Shop_grid_View, name='grid'),
    path('<int:pk>',detail.as_view(),name='detail'),
    path('cart/', views.view_cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/<int:id>/delete/', views.delete_cart_item, name='delete_cart_item'),
    path('wishlist/',views.view_wishlist, name='wishlist_list'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/<int:product_id>/delete', views.delete_wishlist_item, name='delete_wishlist_item'),
    path('checkout/',views.checkout, name='checkout'),
    path('checkout/confirm/',views.order_confirmation,name='confirm'),
]
    
    


