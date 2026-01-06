from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

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


def register_view(request):#регистрация пользователя
    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            return HttpResponse('имя занято,даун')#Проверить, нет ли такого пользователя
        else:
            create_user = User.objects.create_user(username=username, password=password)
            return render(request, 'products/home.html')
    else:
        return render(request, 'products/register_view.html')

def login_view(request):
    return render(request, 'products/login.html')

@login_required
def cartitem(request,product_id):
    if request.method == "POST":
        product_id = Product.objects.get(id=product_id)
        return render(request, 'products/cart.html')
    else:
        return HttpResponse('аутист')












