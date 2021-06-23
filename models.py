from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    queryset = Book.objects.all('id')
    model = Book

class Checkout(models.Model):
    phonenumber = models.PositiveBigIntegerField(blank=False)
    address = CharField(max_length=50, blank=False)
    StateorRegion = CharField(max_length=15, blank=False)
    City = CharField(max_length=15, blank=False)