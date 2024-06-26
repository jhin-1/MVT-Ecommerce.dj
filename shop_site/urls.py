from django.urls import path
from shop_site import views
urlpatterns = [
    path('', views.index, name='home'),
    path('details/<int:id>', views.details, name='details'),
    path('shop', views.shop, name='shop'),
    path('cart/', views.all_cart, name='cart'),
    path('delete_cart/<int:id>/', views.delete_item_cart, name='delete_cart'),
    path('items_cart/<int:id>/', views.items_cart, name='items_cart'),
    path('add_to_cart/', views.add, name='add_to_cart'),
]
