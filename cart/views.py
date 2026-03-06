from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from products.models import Product
from .models import Cart
from .models import CartItem


@login_required
def cart_detail(request):
    cart = request.session.get('cart',{})
    product_ids = cart.keys()
    product = Product.objects.filter(id__in=product_ids)
    




def add_cart(request):
    product_id = request.GET.get('product_id') # берем и смотрим,и запоминаем тот ли товар
    product_id_str = str(product_id)  # переводим все в строки для удобства и JSON

    cart = request.session.get('cart',{}) #создание ключей и словаря

    if product_id_str in cart:#само условие добавление  в корзину
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    request.session['cart'] = cart #возьми список и сохрани под ключом cart
    return redirect('cart_detail')



@login_required
def delete_cart(request): #удаление товара совсем из в корзине
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)

        cart = Cart.objects.get(user=request.user)
        cartitem = CartItem.objects.filter(cart=cart, product=product)

        if cartitem:
            cartitem.delete()
            return redirect('cart:cart_detail')
    return None


@login_required
def change_quantity_cart(request):# изминение количества товаро в корзине
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)

        cart = Cart.objects.get(user=request.user)
        cartitem = CartItem.objects.filter(cart=cart, product=product).first()

        if cartitem:
            if cartitem.quantity > 1:
                cartitem.quantity -= 1
                cartitem.save()
            else:  # quantity == 1
                cartitem.delete()
            return redirect('cart:cart_detail')
        return redirect('cart:cart_detail')
    return None







