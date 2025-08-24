from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("flavours",views.flavours,name='flavours'),
    path("cake",views.cake,name='cake'),
    path("family",views.family,name='family')

]