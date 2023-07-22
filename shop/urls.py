from django.urls import path
from .views import ShopView,detail


urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('<int:pk>',detail.as_view(),name='detail'),
    

]
