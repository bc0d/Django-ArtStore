from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request) :
    return render(request, "home.html")

def about(request) :
    return render(request, 'about.html')

def contact(request) :
    return render(request, 'contact.html')

def products(request) :
    return render(request, 'products.html')

def cart(request) :
    return render(request, 'cart.html')

def services(request) :
    return render(request, 'services.html')

