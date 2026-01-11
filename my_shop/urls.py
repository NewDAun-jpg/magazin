from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('product/<int:product_id>/', views.adres, name='product_detail'),
    path('register/', views.register_view, name='register'),
    path('cartitem/<int:product_id>/', views.cartitem, name='cart_item')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns = [
    #path('products|/',include('products.urls'))
    #path('my_shop/',include('my_shop.urls'))