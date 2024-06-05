from django.urls import path
from shop_site import views
urlpatterns = [
    path('home', views.index, name='index'),
    path('details/<int:id>/', views.details, name='details'),
    path('shop', views.shop, name='shop'),
    path('cart', views.cart, name='cart'),
]
