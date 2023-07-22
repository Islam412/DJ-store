from django.urls import path
from . views import contact


urlpatterns = [
    path('', contact.as_view(), name='shop'),
]
