from django.urls import path
from .views import ShopView,detail ,  Shop_grid_View , detail
from . import views

urlpatterns = [
    path('', Shop_grid_View, name='shop'),
    path('category/<int:category_id>/', views.ShopView, name='shop_by_category'),
    path('list', ShopView, name='grid'),
    path('grid/category/<int:category_id>/', views.Shop_grid_View, name='grid_by_category'),
    path('grid/category/<int:category_id>/<int:sub_id>/', views.Shop_grid_View, name='grid_by_subcategory'),
    path('<int:pk>',detail,name='detail'),
    path('cart/', views.view_cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/<int:id>/delete/', views.delete_cart_item, name='delete_cart_item'),
    path('wishlist/',views.view_wishlist, name='wishlist_list'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/<int:product_id>/delete', views.delete_wishlist_item, name='delete_wishlist_item'),
    path('checkout/',views.checkout, name='checkout'),
    path('checkout/confirm/',views.order_confirmation,name='confirm'),
]
    
    


