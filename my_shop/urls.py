from django.contrib import admin 
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('', include('products.urls')),
    path('',include('cart.urls')),
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:#настройка для полноценной работы изображений для продуктов
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

