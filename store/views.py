from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import login, logout

# Create your views here.


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html',{'products' : products})


def about(request):
    return render(request, 'about.html',{})

def logout_user(request):
    logout(request)
    return redirect('home')

def login_user(request):
    return redirect('home')