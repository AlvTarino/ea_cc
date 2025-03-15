# products.py
from django.db import models
# from django.conf import settings


class Product(models.Model):
    CATEGORIES = [('coffee', 'Coffee'), ('cocoa', 'Cocoa')]
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# The Product model has the following fields:
# name: The name of the product.
# description: A description of the product.
# price: The price of the product.
# category: The category of the product.
# stock: The number of items in stock.
# image: An image of the product.
# created_at: The date and time the product was created.
# updated_at: The date and time the product was last updated.
# The __str__ method returns the name of the product when it's converted to a
# string.
# The CATEGORIES constant is a list of tuples with the available categories
# for the products.
# The image field is an ImageField, which allows you to upload an image for
# the product.
# The upload_to argument specifies the directory where the images will be
# uploaded.
# In this case, the images will be uploaded to the products/ directory inside
# the MEDIA_ROOT directory.
# The created_at and updated_at fields are DateTimeFields that are
# automatically set when the product is created or updated.
# The Product model is used to represent the products available in the shop.
# The Order model is used to represent the orders placed by users.
# The OrderItem model is used to represent the items in each order.
# The Order model has a ForeignKey to the User model, which is the user who
# placed the order.
# The products field is a ManyToManyField to the Product model through the
# OrderItem model.
# The OrderItem model has a ForeignKey to the Order and Product models, and it
# also has a quantity and price field.
# The quantity field is the number of products ordered, and the price field is
# the price of the product at the time the order was placed.
# The Order model also has a total field, which is the total price of the
# order.
# The status field is a CharField with choices for the order status.
# The created_at field is a DateTimeField that is automatically set when the
# order is created.
# The Order model has a __str__ method that returns the user's username and
# the order status.
# The OrderItem model has a __str__ method that returns the product name and
# the quantity ordered.
# The Order model has a get_total method that calculates the total price of
# the order.
# The Order model has a get_absolute_url method that returns the URL of the
# order detail page.
# The OrderItem model has a get_cost method that calculates the cost of the
# item.
# The OrderItem model has a get_absolute_url method that returns the URL of the
# product detail page.
# The Order model has a get_status_display method that returns the human-
# readable name of the order status.
# The Order model has a get_items method that returns the items in the order.
# The Order model has a get_items_count method that returns the total number of
# items in the order.
# The Order model has a get_items_total method that returns the total price of
# the items in the order.
# The Order model has a get_items_price method that returns the price of the
# items in the order.
# The Order model has a get_items_quantity method that returns the quantity of
# the items in the order.
# The Order model has a get_items_cost method that returns the cost of the
# items in the order.
# The Order model has a get_items_weight method that returns the weight of the
# items in the order.
# The Order model has a get_items_shipping method that returns the shippingcost
# of the items in the order.
# The Order model has a get_items_discount method that returns the discount of
# the items in the order.
# The Order model has a get_items_tax method that returns the tax of the items
# in the order.
# The Order model has a get_items_total_price method that returns the total
# price of the items in the order.
