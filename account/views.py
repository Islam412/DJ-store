# custom_user/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str

from .models import CustomUser
from django.db.models import Q 
from django.contrib.auth import get_user_model
from order.models import Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .CustomUserBackend.backends import CustomUserBackend 
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.contrib import messages
from .models import CustomUser
from django.utils.http import urlsafe_base64_decode
from django.urls import reverse


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']

        user = CustomUser.objects.create_user(email=email, name=name, password=password)

        # Generate a unique token for email verification
        token = default_token_generator.make_token(user)

        # Send verification email
        activation_url = request.build_absolute_uri(reverse('activate', args=[urlsafe_base64_encode(force_bytes(user.pk)), token]))
        subject = 'Activate Your Account'
        message = render_to_string('account/activation_email.html', {
            'user': user,
            'activation_url': activation_url,
        })
        send_mail(subject, message, 'masterkhaled33@gmail.com', [email])

        return render(request, 'account/email_verification.html', {'email': email})

    return render(request, 'account/register.html')



def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()  # Decode bytes to string
        user = CustomUser.objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return render(request, 'account/activation_success.html')
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        pass
    return render(request, 'account/activation_failed.html')



def signin(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'account/login.html', {'error': 'Invalid credentials'})

    return render(request, 'account/login.html')




def signout(request):
    logout(request)
    # Redirect to a success page or any other appropriate view
    return redirect('/')



@login_required
def account(request):
    user = request.user
    user_orders = user.orders.all() if hasattr(user, 'orders') else []

    if request.method == 'POST':
        if 'change_password' in request.POST:
            old_password = request.POST.get('old_password')
            new_password1 = request.POST.get('new_password1')
            new_password2 = request.POST.get('new_password2')

            if user.check_password(old_password) and new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                messages.success(request, 'Password changed successfully.')
            else:
                messages.error(request, 'Password change failed. Please check your input.')

            return redirect('/')  # Redirect to account detail page

    context = {
        'user': user,
        'user_orders': user_orders,
    }
    return render(request, 'account/account.html', context)



