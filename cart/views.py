from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from products.models import Product



@login_required
def add_cart(request):
    if request.method == 'GET':
        







@login_required
def change_cart(request,product_id):
    if request.method == 'GET':
        pass



@login_required
def delet_cart(request):
    if request.method == 'GET':
        pass
