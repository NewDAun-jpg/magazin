from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Product


def home(request):#главная страница
    products = Product.objects.all()
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'products/home.html', {'page_obj': page_obj})

def product_detail(request,product_id):#
     product= Product.objects.get(id=product_id)
     return render(request, 'products/product_detail.html', {'product': product})

@login_required
def cartitem(request,product_id):#корзина
    if request.method == "POST":
        product_obj = Product.objects.get(id=product_id)
        return render(request, 'products/cart.html')
    else:
        return HttpResponse(status=503)

def delivery_detail(request):
    return render(request, 'products/delivery_detail.html')

def Wishlist(request):
    pass













