from django.urls import path
from shop_site import views
urlpatterns = [
    path('', views.index, name='index')
]
