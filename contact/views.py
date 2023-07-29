from django.shortcuts import render
from .models import Info
from django.conf import settings
from django.core.mail import send_mail


def send_massege(request):

    if request.method == "POST":
        name= request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        recipient_list = ['masterkhaled33@gmail.com', 'khmo492007@gmail.com', 'khaled.mohamed.tallat@gmail.com']
        send_mail(
            name,
            message,
            settings.EMAIL_HOST_USER,
            recipient_list,
        )
    
    myinfo=Info.objects.first()
    return render(request,'contact/contact.html',{'myinfo':myinfo})