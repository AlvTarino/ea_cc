# shop/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderItem


@receiver(post_save, sender=OrderItem)
def update_inventory(sender, instance, created, **kwargs):
    if created:
        instance.product.stock -= instance.quantity
        instance.product.save()

# This is a signal handler that listens for the post_save signal of the
# OrderItem model. When a new OrderItem is created, it updates the stock
# quantity of the associated product by subtracting the quantity of the
# OrderItem. This ensures that the product's stock is updated whenever an
# order is placed.
# The @receiver decorator is used to connect the signal handler to the
# post_save signal of the OrderItem model. The handler function takes the
# sender, instance, created, and kwargs arguments, where instance is the
# newly created OrderItem object. The handler updates the stock quantity of
# the associated product and saves the changes.
# This signal handler helps maintain accurate inventory levels by automatically
# updating the stock quantity of products when orders are placed. It ensures
# that the stock levels are always up-to-date and prevents overselling of
# products.
