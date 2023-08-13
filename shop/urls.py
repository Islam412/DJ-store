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
    path('add_product/',views.add_product,name='add_product')
]
    
    


