from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import SignUpForm
# Create your views here.




def viewProduct(request, productPk):
    product = Product.objects.get(id=productPk)

    return render(request, 'product.html', {'product': product })


def category(request, queryCategory):

    query = queryCategory.replace('-','')
    try:
        category = Category.objects.get(name=query)
    except:
        messages.success(request, ("there are no product for this category"))
    
    products = Product.objects.filter(Category=category)

    return render(request, 'category.html', {'products': products , 'category' : category })




def home(request):
    products = Product.objects.all()
    try:
        categories = Category.objects.all()
    except:
        messages.success(request, ("There are no categories listed"))
    return render(request, 'home.html',{'products' : products, 'categories':categories})



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
    form = SignUpForm
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, (f"Thank you for registering {username}"))
                return redirect('homePage')
            else:
                messages.success(request, ("an error ocurred"))
                return redirect('homePage')
        else:
            error_messages = [message for messages in form.errors.values() for message in messages]
            return render(request, 'register.html', {'form': form, 'error_messages': error_messages})
    else:
        return render(request, 'register.html', {'form': form})