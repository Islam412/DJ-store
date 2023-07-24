from django.urls import path
from .views import ShopView,detail
from . import views

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('<int:pk>',detail.as_view(),name='detail'),
    path('cart/', views.view_cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/<int:id>/delete/', views.delete_cart_item, name='delete_cart_item'),
    path('wishlist/',views.wishlistitem_list, name='wishlist_list'),
    path('wishlist/add/<int:id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/delete/<int:id>/', views.delete_wishlist_item, name='delete_wishlist_item'),
]
    
    


