from django.test import TestCase
from django.urls import reverse
from .models import Cart,CartItem
from products.models import Product,Category
from django.contrib.auth.models import User

class CartTestAdd(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='papa', email='', password='')
        self.category = Category.objects.create(name='Category')
        self.product = Product.objects.create(
            name='Tovar',
            price=5.30,
            description='Tovar',
            category=self.category
        )




