
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('product/', views.ProductsList, name='product'),
    path('deleteProduct/<int:pk>/', views.DeleteProduct, name='deleteProduct'),
    path('editProduct/<int:pk>/', views.EditProduct, name='editProduct'),
    path('additem', views.AddProduct, name='additem'),
    path('viewitem', views.ViewProduct, name='viewitem'),

    path('acoounts/', views.Acoounts, name='acoounts'),
    path('login/', views.UserLogin,  name='login'),

    path('dashboard/', views.Dashboard,  name='dashboard'),
    
]

