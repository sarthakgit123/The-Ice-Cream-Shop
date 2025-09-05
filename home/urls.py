from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("flavours",views.flavours,name='flavours'),
    path("addtocart/<int:product_id>/", views.addtocart, name="addtocart"),
    path("cart/", views.cart, name="cart"),
    path("update_cart/<int:product_id>/<str:action>/", views.update_cart, name="update_cart"),

]