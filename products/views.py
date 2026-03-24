from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Product, Wishlist


def home(request):#главная страница
    products = Product.objects.all() #вызываем все обьекты
    paginator = Paginator(products, 10) # создаем пагинатор -это разделение на страницы(чтобы не висло)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'products/home.html', {'page_obj': page_obj})


def product_detail(request,product_id):#
     product= Product.objects.get(id=product_id)
     return render(request, 'products/product_detail.html', {'product': product})


def delivery_detail(request):
    return render(request, 'products/delivery_detail.html')


@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'products/wishlist_page.html', {'wishlist_items': wishlist_items})


@login_required
def add_to_wishlist(request):
    product_id = request.GET.get('product_id')  # берем и смотрим,и запоминаем тот ли товар
    product_id_str = str(product_id)  # переводим все в строки для удобства и JSON

    wishlist = request.session.get('wishlist', {})

    if product_id_str in wishlist:
        wishlist[product_id_str] = 1

    request.session['wishlist'] = wishlist
    request.session.modified = True
    request.session.save()
    return redirect('wishlist_page')



@login_required
def delet_to_wishlist(request):
    pass














