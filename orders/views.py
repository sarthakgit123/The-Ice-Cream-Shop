from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction

from .models import Cart, CartItem, Order, OrderItem
from products.models import Product

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, "Item added to cart")
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.select_related('product')

    total = sum(item.product.price * item.quantity for item in items)

    return render(request, 'orders/cart.html', {
        'cart': cart,
        'items': items,
        'total': total
    })

@login_required
def update_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)

    quantity = int(request.POST.get('quantity', 1))

    if quantity > 0:
        item.quantity = quantity
        item.save()
    else:
        item.delete()

    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()

    messages.success(request, "Item removed")
    return redirect('view_cart')

@login_required
@transaction.atomic
def place_order(request):
    cart = get_object_or_404(Cart, user=request.user)
    items = cart.items.select_related('product')

    if not items.exists():
        messages.error(request, "Cart is empty")
        return redirect('view_cart')

    total_price = 0

    # Calculate total
    for item in items:
        total_price += item.product.price * item.quantity

    # Create Order
    order = Order.objects.create(
        user=request.user,
        total_price=total_price,
        status='pending'
    )

    # Create Order Items
    order_items = []
    for item in items:
        order_items.append(OrderItem(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price  # snapshot price
        ))

    OrderItem.objects.bulk_create(order_items)

    # Clear Cart
    items.delete()

    messages.success(request, "Order placed successfully!")
    return redirect('order_detail', order_id=order.id)

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    items = order.items.select_related('product')

    return render(request, 'orders/order_detail.html', {
        'order': order,
        'items': items
    })