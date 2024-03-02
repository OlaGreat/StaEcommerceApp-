from django.shortcuts import render

# Create your views here.


def summary(request):
    return render(request, 'cart_summary.html', {})

def add(request, pk):
    pass


def delete(request, pk):
    pass

def update(request, pk):
    pass

 