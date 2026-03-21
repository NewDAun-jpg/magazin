from django.urls import path
from .import views

app_name = "products"

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('delivery/', views.delivery_detail, name='delivery'),
    path('wishlist/',views.wishlist, name='wishlist'),
    path('add_wishlist/',views.add_to_wishlist, name='add_wishlist'),
    path('delet_wishlist/',views.delet_to_wishlist, name='delet_wishlist'),
]