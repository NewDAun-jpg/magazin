from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from typing import Any

from products.models import Product, Category
from .models import CartItem


class CartTestAdd(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.cart = None

    def setUp(self):
        self.user = User.objects.create_user(username='papa', email='', password='')
        self.category = Category.objects.create(name='Category')
        self.product = Product.objects.create(
            name='Tovar',
            price=500,
            description='Tovar',
            category=self.category
        )

    def test_add_cart_first_time(self):
        self.client.force_login(self.user) #регестририуме клиента
        response = self.client.get(reverse('add_cart'), {'product_id':self.product.id})#наш клиент видит,что в корзину добавил то,что хотел
        self.assertEqual(response.status_code, 200)#вывод 200 что все работает
        cart_item = CartItem.objects.get(cart_user=self.cart, product=self.product).first()#связывает пользователя и корзину и так же продуктыи продукты пользователя
        self.assertEqual(cart_item.quantity, 1)#если все нормально,то количество товаров ==1







