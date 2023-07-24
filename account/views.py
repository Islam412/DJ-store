# custom_user/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        img = request.FILES.get('img')
        age = request.POST.get('age')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Save the new user to the database
        user = CustomUser(
            name=name,
            img=img,
            age=age,
            email=email,
            password=password,
            role=role
        )
        user.save()

        # Redirect to a success page or any other appropriate view
        return redirect('login')


    return render(request, 'account/register.html')

def signin(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, email=Name, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page or any other appropriate view
            return redirect('/')
        else:
            # Invalid credentials, show an error message or redirect back to the login page
            return render(request, 'account/login.html', {'error': 'Invalid credentials'})

    return render(request, 'account/login.html')

def signout(request):
    logout(request)
    # Redirect to a success page or any other appropriate view
    return redirect('/')
