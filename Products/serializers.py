
from rest_framework import serializers
from .models import Product, Cart

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('__all__')
