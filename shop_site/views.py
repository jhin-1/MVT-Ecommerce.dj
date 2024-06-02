from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def index(request):
    context = {
        "id_product": Product.objects.all(),
        "category": MainCategory.objects.all(),
    }
    return render(request, 'pages/index.html', context)


def details(request):
    return render(request, 'pages/details.html')


def shop(request):
    return render(request, 'pages/shop.html')


def cart(request):
    return render(request, 'pages/cart.html')