from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})

def adres(request,product_id):
    adres = Product.objects.get(id=product_id)
    return render(request, 'products/product_detail.html', {'product': adres})

@login_required
def cartitem(request,product_id):
    if request.method == "POST":
        product_id = Product.objects.get(id=product_id)
        return render(request, 'products/cart.html')
    else:
        return HttpResponse('аутист')












