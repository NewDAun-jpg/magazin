from django.db import models
from django.contrib.auth.models import User
from typing import Any



class Category(models.Model):#категории
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):#главный класс
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT,blank=True) #PROTECT - пока есть товары категорию не удалить
    image = models.ImageField(upload_to='products/', null=True, blank=True)


    def __str__(self):
        return self.name # показывать  продукт


class Wishlist(models.Model):  # Избранное/лист желания
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)


    def __str__(self):
        return f'Избранное {self.user.username}:'

    class Meta:
        unique_together = ('user', 'products')




