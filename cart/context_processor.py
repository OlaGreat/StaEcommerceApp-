from .cart import Cart
from store .models import Category

def cart(request):
    return {'cart': Cart(request)}


def category(request):
    categories = Category.objects.all()

    return {'categories': categories}