from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.generic.edit import FormMixin
from django.views.generic import TemplateView
from products.models import Product
from .models import *
from .cart import Cart
from .forms import *


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            update_quantity=cd['update']
        )
    data = {
        'price': product.price,
        'total_price': cart.get_total_price()
    }
    data.update(request.POST)
    return JsonResponse(data)


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    # print(cart.get_total_price())
    return JsonResponse({
        'product_id': product.id,
        'total_price': cart.get_total_price()
    })


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                ProductInOrder.objects.create(order=order,
                                              product=item['product'],
                                              price=item['price'],
                                              quantity=item['quantity'])
            cart.clear()
            return render(request, 'order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'order/create.html', {'cart': cart, 'form': form})

