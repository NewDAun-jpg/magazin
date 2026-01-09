from django.contrib import admin
from .models import Category, Product, UniqueUser, Wishlist, Cart, CartItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(UniqueUser)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(CartItem)