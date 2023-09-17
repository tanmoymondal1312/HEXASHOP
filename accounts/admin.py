from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_seller','is_staff', 'is_superuser', 'date_joined')  # Include 'is_seller' in the list_display
    list_filter = ('is_seller','is_staff', 'is_superuser', 'date_joined')  # Include 'is_seller' in the list_filter
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),       
        ('Custom Fields', {'fields': ('is_seller',)}),  # Include 'is_seller' in the 'Custom Fields' section
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
