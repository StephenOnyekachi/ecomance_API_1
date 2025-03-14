
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import ProductsSerializers, CartSerializers
from .models import Product, Cart

# Create your views here.

class CreateProducts(APIView):
    def post(self, request):
        serializer = ProductsSerializers(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response({'message':'user created successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    
class ViewProduct(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductsSerializers(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EditeProduct(APIView):
    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductsSerializers(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeleteProduct(APIView):
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ProductCount(APIView):
    def get(self, request):
        product = Product.objects.count()
        total={
            'count':product,
        }
        return Response(total, status=status.HTTP_200_OK)


