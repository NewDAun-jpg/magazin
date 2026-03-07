from django.shortcuts import redirect, render
from products.models import Product


def cart_detail(request):
    cart = request.session.get('cart', {})
    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)

    # Создаём список элементов
    items = []
    total = 0
    for product in products:
        quantity = cart.get(str(product.id), 0)
        if quantity > 0:
            items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': product.price * quantity
            })
            total += product.price * quantity

    return render(request, 'cart_detail.html', {'items': items, 'total': total})
    




def add_cart(request):
    product_id = request.GET.get('product_id') # берем и смотрим,и запоминаем тот ли товар
    product_id_str = str(product_id)  # переводим все в строки для удобства и JSON

    cart = request.session.get('cart',{}) #создание ключей и словаря

    if product_id_str in cart:#само условие добавление  в корзину
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    request.session['cart'] = cart #возьми список и сохрани под ключом cart
    return redirect('cart:cart_detail')



def delete_cart(request): #удаление товара совсем из в корзине
    product_id = request.GET.get('product_id')
    product_id_str = str(product_id)
    cart = request.session.get('cart',{})

    if product_id_str not in cart:
        request.session['cart'] = cart
    else:
        cart[product_id_str] -= 1
        if 
        return redirect('cart:cart_detail')



def change_quantity_cart(request):# изминение количества товаро в корзине
    product_id = request.GET.get('product_id')
    product_id_str = str(product_id)
    request.session.get('cart', {})
    if product_id_str:
        if product_id_str.quantity > 1:
            product_id_str.quantity -= 1
            product_id_str.save()
        else:  # quantity == 1
            product_id_str.delete()
            return redirect('cart:cart_detail')
        return redirect('cart:cart_detail')
    return None







