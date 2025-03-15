# inventory/admin.py
from django.contrib import admin
from .models import StockAdjustment


@admin.register(StockAdjustment)
class StockAdjustmentAdmin(admin.ModelAdmin):
    list_display = ('product', 'adjustment', 'reason', 'date')
    list_filter = ('product', 'date')
    search_fields = ('product', 'reason')
    date_hierarchy = 'date'
    ordering = ('-date',)
    actions = ['export_as_csv']
