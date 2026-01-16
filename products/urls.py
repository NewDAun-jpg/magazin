from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('product/<int:product_id>/', views.adres, name='product_detail'),
    path('cartitem/<int:product_id>/', views.cartitem, name='cart_item')
]