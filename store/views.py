from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html',{'products' : products})



def about(request):
    return render(request, 'about.html',{})



def logout_user(request):
    logout(request)
    return redirect('homePage')



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username= username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, (f'Welcome back {username}'))
            return redirect('homePage')
        else:
            messages.success(request, ('invalid user details'))
            return redirect('login')
    else:
        return render(request, 'login.html', {})
    

def register(request):
    
    return render(request, 'register.html', {})