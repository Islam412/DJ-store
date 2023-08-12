# custom_user/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from shop.models import Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        img = request.FILES.get('img')
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        # Save the new user to the database
        user = CustomUser(
            name=name,
            img=img,
            email=email,
            
        )
        user.set_password(password)  # Hash the password before saving
        user.save()

        # Redirect to a success page or any other appropriate view
        return redirect('signin/')  # Use the name of the URL pattern, not the URL itself

    return render(request, 'account/register.html')




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

    return render(request, 'account/account.html', {'user': user, 'user_orders': user_orders})




@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id, user=request.user)
    return render(request, 'account/order_detail.html', {'order': order})



from .forms import EditAccountForm


@login_required
def edit_account(request):
    user = request.user

    if request.method == 'POST':
        form = EditAccountForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('usre_info')  # Redirect to account detail page after successful edit
    else:
        form = EditAccountForm(instance=user)

    return render(request, 'account/account_detail.html', {'form': form})



from .forms import ChangePasswordForm

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/')  # Redirect to account detail page after successful password change
    else:
        form = ChangePasswordForm(user=request.user)

    return render(request, 'account/change_password.html', {'form': form})