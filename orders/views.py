from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # get or create cart
    cart, created = Cart.objects.get_or_create(user=request.user)

    # check if item already exists
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')

from django.shortcuts import render

@login_required
def view_cart(request):
    cart = Cart.objects.filter(user=request.user).first()

    total = 0
    items = []

    if cart:
        items = cart.items.all()
        for item in items:
            total += item.product.price * item.quantity

    return render(request, 'cart.html', {
        'cart_items': items,
        'total': total
    })

from django.db import transaction
from .models import Order, OrderItem

@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user).first()

    if not cart or cart.items.count() == 0:
        return redirect('view_cart')

    with transaction.atomic():  # 🔥 IMPORTANT
        total = 0

        # calculate total
        for item in cart.items.all():
            total += item.product.price * item.quantity

        # create order
        order = Order.objects.create(
            user=request.user,
            total_price=total,
            status='pending'
        )

        # create order items + update stock
        for item in cart.items.all():
            product = item.product

            if product.stock < item.quantity:
                raise Exception(f"{product.name} is out of stock")

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item.quantity,
                price=product.price
            )

            # reduce stock
            product.stock -= item.quantity
            if product.stock == 0:
                product.is_available = False
            product.save()

        # clear cart
        cart.delete()

    return redirect('order_success')

from django.http import HttpResponse

def order_success(request):
    return HttpResponse("Order placed successfully!")
