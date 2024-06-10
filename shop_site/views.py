from django.shortcuts import render, redirect
from django.db.models import Sum
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
    sub_total = Cart.objects.all()
    shipping = 10
    sub = 0
    for total in sub_total:
       sub += total.total_item
    total_summary = int(sub)
    view_cart = {
        "items_cart": Cart.objects.all().order_by("id"),
        "subtotal": sub + shipping,
        "shipping_cost": shipping,
        "total_summary": total_summary,

    }

    return render(request, 'pages/cart.html', view_cart)


def add(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id", 0)
        try:
            get_old = Cart.objects.get(product_id=product_id)
        except:
            get_old = None
        if get_old:
            get_old.items += 1
            get_old.total_item = get_old.product.discount * get_old.items
            get_old.save()
        else:
            add_cart = Cart.objects.create(
                product_id=product_id, items=1

            )
            add_cart.total_item = add_cart.product.discount
            add_cart.save()
    return redirect('cart')


def items_cart(request, id):
    cart_items = Cart.objects.filter(product_id=id).first()
    if request.method == "POST":
        items_quantity = int(request.POST.get("items"))
        if items_quantity > 0:
            if cart_items:
                cart_items.items = items_quantity
                cart_items.total_item = cart_items.product.discount * items_quantity
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
