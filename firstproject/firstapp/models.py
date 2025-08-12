from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

   
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    reservation_time = models.DateTimeField(auto_now=True)
    guest_count = models.PositiveIntegerField()
    comments = models.TextField(max_length=1000)

    