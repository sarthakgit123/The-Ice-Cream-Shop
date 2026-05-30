from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/customer/', views.register_customer, name='register_customer'),
    path('register/vendor/', views.register_vendor, name='register_vendor'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('profile/', views.profile_view, name='profile'),

    path('vendor/update/', views.update_vendor, name='update_vendor'),
    path('vendor/dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
]