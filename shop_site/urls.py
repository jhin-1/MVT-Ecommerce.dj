from django.urls import path
from shop_site import views
urlpatterns = [
    path('home', views.index, name='index'),
    path('details/<int:id>/', views.details, name='details'),
    path('shop', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('delete_cart/<int:id>/', views.delete_item_cart, name='delete_cart'),
    path('add_items/<int:id>/', views.delete_item_cart, name='add_items'),
    path('add_to_cart/', views.add, name='add_to_cart'),
]
