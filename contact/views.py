from django.shortcuts import render,redirect
from .models import Info
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import ListView
# Create your views here.

'''
def contact(request):
    info = Info.objects.first()
    return render(request,'contact.html',{'info':info})
'''

class contact(ListView):
    model = Info
    template_name = 'contact.html'
    context_object_name = 'info'




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

    else:
        return redirect('/')