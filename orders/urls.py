from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.view_cart, name='view_cart'),

    path('add/<int:product_id>/',
         views.add_to_cart,
         name='add_to_cart'),

    path('update/<int:item_id>/',
         views.update_cart_item,
         name='update_cart_item'),

    path('remove/<int:item_id>/',
         views.remove_from_cart,
         name='remove_from_cart'),

    path('place-order/',
         views.place_order,
         name='place_order'),

    path('order/<int:order_id>/',
         views.order_detail,
         name='order_detail'),
]