from django.test import TestCase
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Wishlist,Product

class WishlistTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='john', email='', password='')
        self.wishlist = Wishlist.objects.create(user=self.user)
        self.product = Product.objects.create(
            name='Tovar',
            price=500,
            description='Tovar',
        )

    def test_add_wishlist(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('add_wishlist'))




