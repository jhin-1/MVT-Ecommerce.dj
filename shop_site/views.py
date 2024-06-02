from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def details(request):
    return render(request, 'pages/details.html')


def shop(request):
    return render(request, 'pages/shop.html')


def cart(request):
    return render(request, 'pages/cart.html')