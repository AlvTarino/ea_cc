from django.contrib import admin
from .models import Product, Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Number of empty forms to display
    raw_id_fields = ['product']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ['name']}
    readonly_fields = ['created_at']
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'category')
        }),
        ('Details', {
            'fields': ('description', 'price', 'stock', 'image')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    # In ProductAdmin
    actions = ['restock']

    def restock(self, request, queryset):
        for product in queryset:
            product.stock += 100  # Or set to your restock quantity
            product.save()
    restock.short_description = "Add 100 units to stock"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['user__username', 'id']
    inlines = [OrderItemInline]
    readonly_fields = ['created_at']
    actions = ['mark_as_paid', 'mark_as_shipped']

    def mark_as_paid(self, request, queryset):
        queryset.update(status='paid')
    mark_as_paid.short_description = "Mark selected orders as paid"

    def mark_as_shipped(self, request, queryset):
        queryset.update(status='shipped')
    mark_as_shipped.short_description = "Mark selected orders as shipped"

    fieldsets = (
        (None, {
            'fields': ('user', 'status')
        }),
        ('Payment Info', {
            'fields': ('total', 'payment_method')
        }),
        ('Dates', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'get_total_price']
    autocomplete_fields = ['product']

    def get_total_price(self, obj):
        return obj.product.price * obj.quantity
    get_total_price.short_description = 'Total Price'


# Optional: Customize admin site header
admin.site.site_header = "East Africom Admin"
admin.site.site_title = "East Africom Admin Portal"
admin.site.index_title = "Welcome to East Africom Admin"
