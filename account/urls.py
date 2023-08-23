from django.urls import path
from . import views


urlpatterns = [
    path('',views.signup,name='signup'),
    path('user/',views.account,name='user'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.signout,name='logout'),
    path('activate/<uidb64>/<token>/', views.activate_account, name='activate'),
]

