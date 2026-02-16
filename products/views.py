from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Product, Wishlist


def home(request):#главная страница
    products = Product.objects.all()
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'products/home.html', {'page_obj': page_obj})


def product_detail(request,product_id):#
     product= Product.objects.get(id=product_id)
     return render(request, 'products/product_detail.html', {'product': product})


def delivery_detail(request):
    return render(request, 'products/delivery_detail.html')


@login_required
def add_to_wishlist(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        product = Product.objects.get(id=product_id)  # нужно ловить ошибку, если товара нет

        # Пытаемся найти существующую запись
        wish_item = Wishlist.objects.filter(user=request.user, product=product).first()

        if wish_item:
            # Запись есть — увеличиваем количество
            wish_item.quantity += 1
            wish_item.save()
        else:
            # Записи нет — создаём новую
            Wishlist.objects.create(user=request.user, product=product, quantity=1)

        # возращаем старницу
        return redirect('wishlist_page')














