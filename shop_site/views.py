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


def all_cart(request):
    view_cart = {
        "items_cart": Cart.objects.all().order_by("id"),

    }

    return render(request, 'pages/cart.html', view_cart)


def add(request):
    if request.method == "POST":
        add_cart = Cart.objects.create(
            product_id=request.POST.get("product_id"), items=1

        )
        add_cart.total = add_cart.product.discount
        add_cart.save()
    return redirect('cart')


def items_cart(request, id):
    cart_items = Cart.objects.filter(product_id=id).first()
    if request.method == "POST":
        items_quantity = int(request.POST.get("items"))
        if items_quantity > 0:
            if cart_items:
                cart_items.items = items_quantity
                cart_items.total = cart_items.product.discount * items_quantity
                cart_items.save()
        else:
            cart_items.delete()
            return redirect('cart')

    return redirect('cart')


def delete_item_cart(request, id):
    cart_item = Cart.objects.filter(product_id=id).first()
    if cart_item:
        cart_item.delete()
    return redirect('cart')


# def cart_summary(request):
