from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']

        if password1 == password2:
            user = CustomUser.objects.create_user(username=username, email=email, password=password1)
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Passwords do not match.')
    
    return render(request, 'account/register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'account/login.html')


def signout(request):
    logout(request)
    return redirect('home')
