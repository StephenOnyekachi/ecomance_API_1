
from django.urls import path
from . import views

urlpatterns = [
    path('createproduct/', views.CreateProducts.as_view(), name='createproduct'),
    path('products/', views.ViewProduct.as_view(), name='products'),
    path('countproduct/', views.ProductCount.as_view(), name='countproduct'),
    path('editproduct/<int:pk>/', views.EditeProduct.as_view(), name='editproduct'),
    path('deleteproduct/<int:pk>', views.ViewProduct.as_view(), name='deleteproduct'),
    
    #  path('carts/', views.CartList.as_view(), name='carts'),
    #  path('cartInfo/<int:pk>', views.CartInfo.as_view(), name='cartInfo'),

]

