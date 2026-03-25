from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='home'),

    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    # Vendor
    path('add/', views.add_product, name='add_product'),
    path('update/<int:product_id>/', views.update_product, name='update_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),

    path('my-products/', views.vendor_products, name='vendor_products'),
]