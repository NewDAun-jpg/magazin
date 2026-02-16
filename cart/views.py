from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from products.models import Product










@login_required
def cartitem(request,product_id):#корзина
    if request.method == "POST":
        product_obj = Product.objects.get(id=product_id)
        return render(request, 'products/cart.html')
    else:
        return HttpResponse(status=503)
