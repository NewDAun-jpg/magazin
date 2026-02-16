from django.urls import path
from .import views

app_name = "cart"

urlpatterns = [
    path('cartitem/<int:product_id>/', views.cartitem, name='cart_item'),
]