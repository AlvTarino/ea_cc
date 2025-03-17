# inventory/admin.py
from django.contrib import admin
from .models import StockAdjustment


@admin.register(StockAdjustment)
class StockAdjustmentAdmin(admin.ModelAdmin):
    list_display = ('product', 'adjustment', 'previous_quantity',
                    'new_quantity', 'reason', 'adjusted_by', 'created_at')
    list_filter = ('product', 'date', 'reason', 'created_at')
    search_fields = ('product__name', 'reason')
    readonly_fields = ('previous_quantity', 'new_quantity', 'created_at')
    autocomplete_fields = ('product',)
    date_hierarchy = 'date'
    ordering = ('-created_at',)
    actions = ['export_as_csv']

    def save_model(self, request, obj, form, change):
        if not change:  # Only set user on creation
            obj.adjusted_by = request.user
        super().save_model(request, obj, form, change)
