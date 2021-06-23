from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import serializers
from .models import Book

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CheckoutView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = BookSerializer

class CheckoutCartView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
