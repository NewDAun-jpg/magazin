from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import user_login_failed


from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})

def about(request):
    return render(request, 'products/about.html')

def contact(request):
    return render(request, 'products/contact.html')

def adres(request,product_id):
    adres = Product.objects.get(id=product_id)
    return render(request, 'products/product_detail.html', {'product': adres})


def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('username').get('password')# Получить username и password из request.POST
        if request.user.is_authenticated:
            return  render(request,'products/home.html') #Проверить, нет ли такого пользователя
        else:
            return  HttpResponse('зарегайся сначаал идиот')# Если есть — вернуть ошибку
        # Если нет — создать пользователя, залогинить
        pass
    else:
        return render(request, 'products/register_view.html')

def login_view(request):
    return render(request, 'products/login.html')






