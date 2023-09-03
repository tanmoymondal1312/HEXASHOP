from django.contrib import admin
from .models import Product, Reviews

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ['product_name', 'price', 'category', 'stock', 'created_date', 'modified_date', 'is_available']

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['user_username', 'product_product_name', 'rating', 'created_date', 'modified_date']

    def user_username(self, obj):
        return obj.user.username

    def product_product_name(self, obj):
        return obj.product.product_name

admin.site.register(Product, ProductAdmin)
admin.site.register(Reviews, ReviewsAdmin)
