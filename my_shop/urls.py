from django.contrib import admin
from django.urls import path
from products.views import home, register_view
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('product/<int:product_id>/' ,views.adres,name='product_detail'),
    path('register/',views.register_view,name='register'),
    path('cartitem/<int:product_id>/', views.cartitem, name='cart_item')
]