from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from products.models import Product
from .models import Cart
from .models import CartItem



@login_required
def add_cart(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id') #берем id из бд
        product = Product.objects.get(id=product_id) #проверка на то ли взяли

        usercart

        #проверка на нахождение записи
        cartitem = CartItem.objects.get(user=request.user, product=product)











@login_required
def change_cart(request,product_id):
    if request.method == 'GET':
        pass



@login_required
def delet_cart(request):
    if request.method == 'GET':
        pass
