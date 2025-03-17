from django.db import models
# from django.contrib.auth import get_user_model
from shop.models import Product
from django.conf import settings


User = settings.AUTH_USER_MODEL


class StockAdjustment(models.Model):
    ADJUSTMENT_TYPES = [
        ('restock', 'Restock'),
        ('damage', 'Damage/Loss'),
        ('correction', 'Quantity Correction'),
        ('transfer', 'Warehouse Transfer'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='adjustments')
    adjustment = models.IntegerField(help_text="Positive for additions, "
                                               "negative for deductions")
    previous_quantity = models.IntegerField(editable=False)
    new_quantity = models.IntegerField(editable=False)
    reason = models.CharField(max_length=20, choices=ADJUSTMENT_TYPES)
    notes = models.TextField(blank=True)
    adjusted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True, editable=False, db_index=True)

    def __str__(self):
        return (f"{self.product.name} - "
                f"{self.get_reason_display()}({self.adjustment})")

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Stock Adjustment'
        verbose_name_plural = 'Stock Adjustments'
