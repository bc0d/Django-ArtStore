from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request) :
    return render(request, "home.html")

def about(request) :
    return render(request, 'about.html')

def contact(request) :
    return render(request, 'contact.html')

def products(request) :
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'products.html', context)

def cart(request) :
    return render(request, 'cart.html')

def checkout(request) :
    return render(request, 'checkout.html')

def services(request) :
    return render(request, 'services.html')

