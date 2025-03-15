from .orders import Order, OrderItem
from .products import Product
# Replace 'Product' with the actual classes or functions you need

# The __init__.py file in the shop/models directory imports the Order and
# Product
# models from the orders.py and products.py files, respectively. This allows
# you to
# import the models from the shop.models module directly, without having to
# specify
# the file name. For example, you can import the Order model like this:
# from shop.models import Order
# This makes it easier to organize and manage your models in a Django project.
