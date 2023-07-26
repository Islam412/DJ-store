from django.urls import path
from . import views


urlpatterns = [
    path('',views.signup,name='signup'),
    path('user/',views.User,name='user'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.signout,name='logout'),
]
