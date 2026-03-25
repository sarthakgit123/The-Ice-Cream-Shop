from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User, Vendor

def register_customer(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register_customer')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register_customer')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_customer=True,
            is_vendor=False
        )

        login(request, user)
        return redirect('home')

    return render(request, 'accounts/register_customer.html')

def register_vendor(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        shop_name = request.POST.get('shop_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register_vendor')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_vendor=True,
            is_customer=False
        )

        Vendor.objects.create(
            user=user,
            shop_name=shop_name,
            address=address,
            phone=phone
        )

        login(request, user)
        return redirect('vendor_dashboard')

    return render(request, 'accounts/register_vendor.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # Role-based redirect
            if user.is_vendor:
                return redirect('vendor_dashboard')
            else:
                return redirect('home')

        messages.error(request, "Invalid credentials")
        return redirect('login')

    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    user = request.user

    context = {
        'user': user
    }

    if user.is_vendor:
        context['vendor'] = getattr(user, 'vendor', None)

    return render(request, 'accounts/profile.html', context)


@login_required
def update_vendor(request):
    if not request.user.is_vendor:
        return redirect('home')

    vendor = get_object_or_404(Vendor, user=request.user)

    if request.method == 'POST':
        vendor.shop_name = request.POST.get('shop_name')
        vendor.address = request.POST.get('address')
        vendor.phone = request.POST.get('phone')
        vendor.save()

        messages.success(request, "Vendor profile updated")
        return redirect('profile')

    return render(request, 'accounts/update_vendor.html', {'vendor': vendor})


@login_required
def vendor_dashboard(request):
    if not request.user.is_vendor:
        return redirect('home')

    vendor = get_object_or_404(Vendor, user=request.user)

    return render(request, 'accounts/vendor_dashboard.html', {
        'vendor': vendor
    })
