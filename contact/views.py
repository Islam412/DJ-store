from django.shortcuts import render
from .models import Info
# Create your views here.

def contact(request):
    info = Info.objects.first()
    return render(request,'contact.html',{'info':info})