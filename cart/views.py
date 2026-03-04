from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from products.models import Product
from .models import Cart
from .models import CartItem


@login_required
def cart_detail(request):
    cart = Cart.objects.get(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    total = sum(item.product.price * item.quantity for item in items)
    return render(request, 'cart_detail.html', {'cart': cart, 'items': items, 'total': total})


@login_required
def add_cart(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        if not product_id:
            return redirect('cart_detail')  #можно в иное место релирект

        product = Product.objects.get_object_or_404(id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Теперь проверка
        if cart.pk is None or product.pk is None:
            print("Ошибка: объект не сохранён")
            return redirect('cart_detail')

        cartitem = CartItem.objects.filter(cart=cart, product=product).first()
        if cartitem:
            cartitem.quantity += 1
            cartitem.save()
        else:
            CartItem.objects.create(cart=cart, product=product, quantity=1)
        return redirect('cart_detail')
    return redirect('cart_detail')  # если не GET


@login_required
def delete_cart(request): #удаление товара совсем из в корзине
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)

        cart = Cart.objects.get(user=request.user)
        cartitem = CartItem.objects.filter(cart=cart, product=product)

        if cartitem:
            cartitem.delete()
            return redirect('cart_detail')
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
            return redirect('cart_detail')
        return redirect('cart_detail')
    return None







