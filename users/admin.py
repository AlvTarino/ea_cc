# In your users app admin.py
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser


# @admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        'email', 'username', 'phone', 'is_staff', 'is_superuser', 'is_active'
    ]
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone', 'shipping_address')}),
    )

    # Force admin access
    def has_module_permission(self, request):
        return True  # Override any custom permission checks


admin.site.register(CustomUser, CustomUserAdmin)

# class OrderInline(admin.StackedInline):
#     model = Order # type: ignore
#     extra = 0
#
#
# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ['email', 'username', 'phone', 'is_staff']
#     fieldsets = UserAdmin.fieldsets + (
#         ('Additional Info', {'fields': ('phone', 'shipping_address')}),
#     )
#     inlines = [OrderInline]
#     list_filter = UserAdmin.list_filter + ('phone',)
#
#
# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
# admin.site.register(CustomUser, CustomUserAdmin)
