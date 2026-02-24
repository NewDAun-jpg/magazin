from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from products.models import Product, Category
from .models import CartItem

class CartTestAdd(TestCase):
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
        self.client.force_login(self.user)
        response = self.client.get(reverse('cart:add_cart'), {'product_id': self.product.id})
        # Проверяем, что запрос выполнен успешно
        self.assertEqual(response.status_code, 302)  # если вьюха редиректит, или 200,или 302
        # Получаем элемент корзины и связь пользователя
        cart_item = CartItem.objects.filter(cart__user=self.user, product=self.product).first()
        self.assertIsNotNone(cart_item)
        self.assertEqual(cart_item.quantity, 1)