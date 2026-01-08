
from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.PROTECT)
    image = models.ImageField(upload_to='products/')
    Wishlist = models.ForeignKey('Wishlist',on_delete=models.PROTECT)



    def __str__(self):
        return f'ID:{self.id}'

class Wishlist(models.Model): #избранные товары
    name = models.CharField(max_length=100)
    User =



class UniqueUser(models.Model):#создание пользхователя(главного?)
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True,blank=True)

class Category(models.Model): # тут будет категория товаров
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Cart(models.Model):
    name = models.CharField(max_length=100)
    UniqueUser = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.name}'

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    products = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()








