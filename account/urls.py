from django.urls import path
from . import views


urlpatterns = [
    path('',views.signup,name='signup'),
    path('user/',views.account,name='user'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.signout,name='logout'),
    path('user/<int:order_id>',views.order_detail,name='order_detail'),
    path('user/edit',views.edit_account,name='usre_info'),
    path('user/change-password/', views.change_password, name='change_password'),
]

