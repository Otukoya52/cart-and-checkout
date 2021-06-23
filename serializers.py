from .models import Cart
from .models import Checkout
from django.contrib.auth.models import User
from rest_framework import serializers

#Serializers for the Cart model
class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'author')
        model = Cart

class CheckoutSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('phonenumber', 'address', 'StateorRegion', 'City')
        model = Checkout