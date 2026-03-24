from django.db import models
from django.contrib.auth.models import AbstractUser

# -------------------------
# Custom User Model
# -------------------------
class User(AbstractUser):
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)

    def __str__(self):
        return self.username


# -------------------------
# Vendor Profile
# -------------------------
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor')

    shop_name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shop_name

# Create your models here.
