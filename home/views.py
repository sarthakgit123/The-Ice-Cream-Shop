from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from home.models import Contact
from .models import Product
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse


def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        reviews=request.POST.get('reviews')
        contact=Contact(name=name,email=email,reviews=reviews)
        contact.save()
        messages.success(request, 'Thank you for your feedback....mujhe lund farak nahi padta')
        return redirect('/#mess')
    return render(request,'index.html')
def flavours(request):
    products = Product.objects.all()
    return render(request,'flavours.html',{'products': products})
def addtocart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    pid = str(product_id)

    if pid in cart:
        cart[pid]['quantity'] += 1
    else:
        cart[pid] = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'quantity': 1
        }

    request.session['cart'] = cart
    request.session.modified = True
    messages.success(request, 'Item added to cart')
    return redirect(reverse('flavours') + '#mess')


def cart(request):
    cart = request.session.get('cart', {})
    total = 0

    for pid, item in cart.items():
        # Add subtotal
        item['subtotal'] = item['price'] * item['quantity']

        # Ensure id exists
        if 'id' not in item:
            item['id'] = int(pid)  # pid is string key in session

        total += item['subtotal']

    request.session['cart'] = cart
    request.session.modified = True

    return render(request, 'cart.html', {'cart': cart, 'total': total})


def update_cart(request, product_id, action):
    cart = request.session.get('cart', {})
    pid = str(product_id)

    if pid in cart:
        product_name = cart[pid]['name']  # store name for messages

        if action == "add":
            cart[pid]['quantity'] += 1
            messages.success(request, f"Added one more {product_name} to cart!")

        elif action == "remove":
            cart[pid]['quantity'] -= 1
            if cart[pid]['quantity'] <= 0:
                del cart[pid]
                messages.success(request, f"{product_name} removed from cart")
            else:
                messages.success(request, f"Removed one {product_name} from cart")

        elif action == "delete":
            del cart[pid]
            messages.success(request, f"{product_name} deleted from cart")

        else:
            messages.error(request, "Invalid action")

    else:
        messages.error(request, "Item not found in cart")

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')

    