
import random
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse,JsonResponse
# from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import random
# from .models import *

# for API clients
from .api_client import *
import requests
api_url = 'http://127.0.0.1:8000/'

# for emails
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.

def Home(request):
    return render(request, 'indext.html')

def Dashboard(request):
    return render(request, 'dashboard.html')

def AddProduct(request):
    # data = Products()
    allproducts = AllProducts()
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        picture = request.FILES.get('picture')
        des = request.POST.get('des')

        product_url = (api_url + 'products/createproducts/')
        product_con = {
            'name': name,
            'price': price,
            'des': des,
        }
        files = {
            'picture': picture,
        }
        response = requests.post(product_url, json=product_con,files=files)
        print('status code is ', response.status_code, response.content)
        if response.status_code == 200:
            messages.success(request, f'{name} was added')
            print('status code is ', response.status_code, response.content)
            return redirect('dashboard')
        else:
            messages.error(request, 'there is error uploading this data')
            print('status code is ', response.status_code, response.content)
            return redirect('dashboard')
    context = {
        # 'data': data,
        'allproducts':allproducts,
    }
    return render(request, 'additem.html', context)

def ProductsList(request):
    data = Products()
    context = {
        'data': data,
    }
    return render(request, 'home.html', context)

def ViewProduct(request):
    data = Products()
    context = {
        'data': data,
    }
    return render(request, 'viewitem.html', context)

def DeleteProduct(request, pk):
    pass
    # data = ProductsInfo()
    # if data:
    #     data.delete()
    #     messages.success(f'{data.name} was delete')
    #     return redirect('product')
    
def EditProduct(request, pk):
    allproduct = AllProducts()
    product = Edit_Products()
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')

        product_url = (api_url + 'products/productInfo/')
        product_con = {
            'name': name,
            'price': price,
        }
        response = requests.put(product_url,json=product_con)
        if response.status_code == 201:
            context = {
                'product':product,
                'status':response.status_code,
                'allproduct':allproduct,
            }
            messages.success(f'{name} was updated')
            return render(redirect, 'product', context)
    return render(request, 'edititem.html')

def Acoounts(request):
    data = Users()
    context = {
        'data': data,
    }
    return render(request, 'users.html', context)

def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        login_url = (api_url + 'users/login/')
        login_con = {
            'username': username,
            'password': password,
        }
        response = requests.post(login_url,json=login_con)
        if response.status_code == 201:
            context = {
                'message': 'welcome back',
                'username': username,
                'status':response.status_code,
            }
            return render(request, 'login.html', context)
        else:
            context = {
                'message': 'username or password incorrect',
                'status':response.status_code,
            }
            return render(request, 'login.html', context)
    return render(request, 'login.html')


