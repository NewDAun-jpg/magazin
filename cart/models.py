from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Cart(models.Model):#корзина
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)




class CartItem(models.Model):#товар в корзине(дословно)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    pass

