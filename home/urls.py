from django.urls import path,include
from . import views
urlpatterns=[
    path('search/', views.product_search_view, name='home'),
]