from django.shortcuts import render, redirect
from .models import *


# Create your views here.


def index(request):
    context = {
        "id_product": Product.objects.all(),
        "id_category": Subcategory.objects.all(),
    }
    return render(request, 'pages/index.html', context)


def details(request, id):
    product = {
        "id_product": Product.objects.get(id=id),
    }

    return render(request, 'pages/details.html', product)


def shop(request):
    return render(request, 'pages/shop.html')


def cart(request):
    return render(request, 'pages/cart.html')
