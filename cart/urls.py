from django.urls import path
from .views import view_cart,view_wishlist,delete_cart_item,delete_wishlist_item,add_to_cart,add_to_wishlist

urlpatterns=[
    path('', view_cart, name='cart'),
    path('<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('<int:id>/delete/', delete_cart_item, name='delete_cart_item'),
    path('wishlist/',view_wishlist, name='wishlist_list'),
    path('wishlist/add/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/<int:product_id>/delete', delete_wishlist_item, name='delete_wishlist_item'),
]