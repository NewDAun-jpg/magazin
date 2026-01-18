from django.contrib import admin 
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products import views

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('register/', views.register_view, name='register'),
    path('products/', include('products.urls'))
]

if settings.DEBUG:#настройка для полноценной работы изображений для продуктов
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

