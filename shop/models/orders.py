from django.db import models
from django.conf import settings
from .products import Product


class Order(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'), ('paid', 'Paid'),
                      ('shipped', 'Shipped')]
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.status}'

    def get_total(self):
        return sum(item.price for item in self.orderitem_set.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'
# The Order model has the following
# fields:
# user: A ForeignKey to the User model, which is the user who placed the order.
# products: A ManyToManyField to the Product model through the OrderItem model.
# total: The total price of the order.
# status: The status of the order.
# created_at: The date and time the order was created.
# The STATUS_CHOICES constant is a list of tuples with the available choices
# for the order status.
# The OrderItem model has the following fields:
# order: A ForeignKey to the Order model.
# product: A ForeignKey to the Product model.
# quantity: The number of products ordered.
# price: The price of the product at the time the order was placed.
# created_at: The date and time the order item was created.
# updated_at: The date and time the order item was last updated.
# The __str__ method returns the product name and the quantity ordered.
# The Order model has a get_total method that calculates the total price of the
# order.


# The Order model has a ForeignKey to the User model, which is the user who
# placed the order. The products field is a ManyToManyField to the Product
# model through the OrderItem model. The OrderItem model has a ForeignKey
# to the Order and Product models, and it also has a quantity and price field.
# The quantity field is the number of products ordered, and the price field is
# the price of the product at the time the order was placed.
