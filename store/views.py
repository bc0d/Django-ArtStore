from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

# Home page
def home(request) :
    return render(request, "home.html")

# About page
def about(request) :
    return render(request, 'about.html')

# Contact page
def contact(request) :
    return render(request, 'contact.html')

# All products display page
def products(request) :
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'products.html', context)

# Cart page
def cart(request) :
    if request.user.is_authenticated :
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all
    else :
        items = []
        order = {
            'get_cart_total' : 0,
            'get_cart_items' : 0,
        }
    context = {
        'items' : items,
        'order' : order,
    }
    return render(request, 'cart.html', context)

# Checkout page
def checkout(request) :
    if request.user.is_authenticated :
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all
    else :
        items = []
        order = {
            'get_cart_total' : 0,
            'get_cart_items' : 0,
        }
    context = {
        'items' : items,
        'order' : order,
    }
    return render(request, 'checkout.html', context)


def services(request) :
    return render(request, 'services.html')

