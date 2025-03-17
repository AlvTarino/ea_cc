from django.shortcuts import render
from shop.models import Order


def view_cart(request):
    # Implement cart logic
    return render(request, 'shop/cart.html')


def checkout(request):
    # Implement checkout logic
    return render(request, 'shop/checkout.html')


def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'shop/order_history.html', {'orders': orders})
