from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=250)
    # Add more fields like address, loyalty points, etc.
