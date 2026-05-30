from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home, Login, Register, Profile
    path('', include('accounts.urls')),

    # Cart, Checkout, Orders
    path('orders/', include('orders.urls')),

    # Product-related URLs
    path('products/', include('products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )