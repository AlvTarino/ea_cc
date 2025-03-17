from django.urls import path
from .views import products, orders

app_name = 'shop'

urlpatterns = [
    # Product URLs
    path('products/', products.product_list, name='product_list'),
    path('products/<int:pk>/', products.product_detail, name='product_detail'),

    # Order URLs
    path('cart/', orders.view_cart, name='view_cart'),
    path('checkout/', orders.checkout, name='checkout'),
    path('order-history/', orders.order_history, name='order_history'),
]
