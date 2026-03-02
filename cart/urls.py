from django.urls import path
from .import views

app_name = "cart"

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add_cart/', views.add_cart, name='add_cart'),
    path('delete_cart/', views.delete_cart, name='delete_cart'),
    path('change_quantity_cart/', views.change_quantity_cart, name='change_quantity_cart'),
]