from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):#категории
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):#главный класс
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    

    def __str__(self):
        return f'{self.name} (ID:{self.id})'  # Лучше показывать имя продукта

    def __str__(self):
        return f'{self.user.username}'


class Wishlist(models.Model):  # Избранное/лист желания
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'Избранное {self.user.username}: {self.name}'


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