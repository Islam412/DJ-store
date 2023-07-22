from django.shortcuts import render
from .models import Info
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