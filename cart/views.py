from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product
from django.http import JsonResponse 
from .cart import Cart
from django.contrib import messages

# Create your views here.


def summary(request):
    cart = Cart(request)
    products = cart.get_products()

    product_quantities = cart.get_quantity()

    total_price = cart.cart_total()

    return render(request, 'cart_summary.html', {'cart_products' : products, 'quantity' : product_quantities, 'total_price' : total_price})

def add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        product = get_object_or_404(Product, id=product_id)

        cart.add(product, product_quantity)

        cart_quantity = cart.__len__()

        product = Product.objects.get(pk=product_id)

        messages.success(request, (f' added {product.name} to cart'))



    response = JsonResponse({ 'cart_size': cart_quantity })

    return response




def delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        
        cart.delete(product_id)

        cart_quantity = cart.__len__()


    response = JsonResponse({'cart_size': cart_quantity})

    return response

def update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = request.POST.get('product_quantity')

    

        cart.update(product_id, product_qty)

    


    response = JsonResponse({'product_qty' : product_id})

    return response

 