from django.contrib import admin
from .models import  Product
from .models import Category
from .models import Cart
from .models import CartItem

admin.site.register(Cart)
admin.site.register(CartItem)

admin.site.register(Category)


admin.site.register(Product)



