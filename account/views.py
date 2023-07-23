from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as auth_logout
# Create your views here.

def signup (request):
   
   if request.method == "POST":
      name = request.POST['name']
      email = request.POST['email']
      password1 = request.POST['password']
      password2=request.POST['password2']

      myuser= User.objects.create_user(name,email,password1)
      myuser.first_name=name
      myuser.last_name=name

      myuser.save()
      return redirect('signin')
   return render(request,'account/register.html')



def signin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        
        user = authenticate(request, username=name, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to the home page after successful sign-in
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'account/login.html')  # Render the sign-in template




def logout(request):
    auth_logout(request)
    return redirect('/')