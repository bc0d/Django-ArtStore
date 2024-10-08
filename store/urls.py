from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('cart/', views.cart, name='cart'),
    path('update_item/', views.updateItem, name='update_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('process_order/', views.processOrder, name='process_order'),
]