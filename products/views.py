from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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
    return render(request, 'products/register_view.html')

def login(request):
    return render(request, 'products/login.html')




