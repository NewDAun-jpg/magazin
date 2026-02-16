from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):#корзина
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Корзина пользователя {self.user.username}'


class CartItem(models.Model):#товар в корзине(дословно)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Исправил на единственное число
    quantity = models.PositiveIntegerField(default=1)  # PositiveIntegerField

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'