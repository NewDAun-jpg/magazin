from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})

def product_detail(request,product_id):
     product_dt= Product.objects.get(id=product_id)
     return render(request, 'products/product_detail.html', {'product': product_dt})

@login_required
def cartitem(request,product_id):
    if request.method == "POST":
        product_obj = Product.objects.get(id=product_id)
        return render(request, 'products/cart.html')
    else:
        return HttpResponse(status=503)












