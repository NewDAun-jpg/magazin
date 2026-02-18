from django.urls import path
from .import views

app_name = "cart"

urlpatterns = [
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('delete_cart/<int:product_id>/', views.delete_cart, name='delete_cart'),
    path('change_quantity_cart/<int:product_id>/', views.change_quantity_cart, name='change_quantity_cart'),
]