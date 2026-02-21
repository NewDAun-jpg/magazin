from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from products.models import Product
from .models import Cart
from .models import CartItem



@login_required
def add_cart(request):# добавление в корзину товаров + создание корзины у пользователя
    if request.method == 'GET':
        product_id = request.GET.get('product_id') #берем id из бд
        product = Product.objects.get(id=product_id) #проверка на то ли взяли

        #содание корзины для пользователя
        cart, created = Cart.objects.get_or_create(user=request.user)
        cartitem = CartItem.objects.filter(cart=cart, product=product).first()

        #добавление в корзину товаров
        if cartitem:
            cartitem.quantity += 1
            cartitem.save()
        else:
            cartitem = CartItem.objects.create(cart=cart, product=product, quantity=1)


@login_required
def delete_cart(request): #удаление товара совсем из в корзине
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)

        cart = Cart.objects.get(user=request.user)
        cartitem = CartItem.objects.filter(cart=cart, product=product)

        if cartitem:
            cartitem.delete()


@login_required
def change_quantity_cart(request):# изминение количества товаро в корзине
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)

        cart = Cart.objects.get(user=request.user)
        cartitem = CartItem.objects.filter(cart=cart, product=product).first()

        if cartitem and cartitem.quantity >= 1:
            cartitem.quantity -= 1
            cartitem.save()
        elif cartitem and cartitem.quantity == 0:
            cartitem.delete()







