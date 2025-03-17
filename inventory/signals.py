from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import StockAdjustment


@receiver(pre_save, sender=StockAdjustment)
def calculate_stock_changes(sender, instance, **kwargs):
    """
    Updates product stock and tracks quantity changes before saving adjustment
    """
    if not instance.pk:  # Only for new entries
        product = instance.product
        instance.previous_quantity = product.stock
        instance.new_quantity = product.stock + instance.adjustment
        product.stock = instance.new_quantity
        product.save()
