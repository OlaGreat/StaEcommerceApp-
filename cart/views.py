from django.shortcuts import render, get_object_or_404
from store.models import Product
from django.http import JsonResponse
from .cart import Cart

# Create your views here.


def summary(request):
    return render(request, 'cart_summary.html', {})

def add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product)

        cart_quantity = cart.__len__()


    response = JsonResponse({ 'cart_size': cart_quantity })

    return response




def delete(request, pk):
    pass

def update(request, pk):
    pass

 