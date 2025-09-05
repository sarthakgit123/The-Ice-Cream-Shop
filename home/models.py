from django.db import models
from decimal import Decimal
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=70)
    reviews=models.TextField()

    def __str__(self):
        return f"{self.name}"
class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)  # Changed to IntegerField
    image = models.ImageField(upload_to="products/", blank=True, null=True)  # requires Pillow

    def __str__(self):
        return self.name


