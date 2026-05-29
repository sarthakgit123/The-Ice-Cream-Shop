from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # Products App (Home Page)
    path('', include('products.urls')),

    # Accounts App
    path('accounts/', include('accounts.urls')),

    # Orders App
    path('orders/', include('orders.urls')),
]

# Media files (for product images)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)