from django.test import TestCase
from django.urls import reverse
from .models import Cart,CartItem
from django.contrib.auth.models import User

class CartTestAdd(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='papa', email='', password='')
        self.cart = Cart.objects.create(user=self.user)

