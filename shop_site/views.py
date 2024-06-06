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
    view_cart = {
        "items_cart": Cart.objects.all().order_by("id"),

    }

    return render(request, 'pages/cart.html', view_cart)


def add(request):
    carts = Cart.objects.all().order_by("id")

    context = {
        "items_cart": carts,
    }

    return render(request, 'pages/cart.html', context)


def items_cart(request, id):
    quantity_item = Cart.objects.filter(product_id=id).first()
    if quantity_item:
        quantity_item.items = 0
        quantity_item.save()
    return redirect('cart')


def delete_item_cart(request, id):
    cart_item = Cart.objects.filter(product_id=id).first()
    if cart_item:
        cart_item.delete()
    return redirect('cart')