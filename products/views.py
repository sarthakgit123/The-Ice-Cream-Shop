from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Product
from accounts.models import Vendor

def product_list(request):
    products = Product.objects.all()

    return render(request, 'products/product_list.html', {
        'products': products
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'products/product_detail.html', {
        'product': product
    })

@login_required
def add_product(request):
    if not request.user.is_vendor:
        return redirect('home')

    vendor = get_object_or_404(Vendor, user=request.user)

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')

        Product.objects.create(
            name=name,
            price=price,
            description=description,
            stock=stock,
            image=image,
            vendor=vendor
        )

        messages.success(request, "Product added")
        return redirect('vendor_dashboard')

    return render(request, 'products/add_product.html')


@login_required
def add_product(request):
    if not request.user.is_vendor:
        return redirect('home')

    vendor = get_object_or_404(Vendor, user=request.user)

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')

        Product.objects.create(
            name=name,
            price=price,
            description=description,
            stock=stock,
            image=image,
            vendor=vendor
        )

        messages.success(request, "Product added")
        return redirect('vendor_dashboard')

    return render(request, 'products/add_product.html')

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if product.vendor.user != request.user:
        return redirect('home')

    product.delete()
    messages.success(request, "Product deleted")

    return redirect('vendor_dashboard')

@login_required
def vendor_products(request):
    if not request.user.is_vendor:
        return redirect('home')

    vendor = request.user.vendor
    products = Product.objects.filter(vendor=vendor)

    return render(request, 'products/vendor_products.html', {
        'products': products
    })
@login_required
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if product.vendor.user != request.user:
        return redirect('home')

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.stock = request.POST.get('stock')

        if request.FILES.get('image'):
            product.image = request.FILES.get('image')

        product.save()

        messages.success(request, "Product updated")
        return redirect('vendor_dashboard')

    return render(request, 'products/update_product.html', {
        'product': product
    })