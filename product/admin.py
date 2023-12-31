from django.contrib import admin
from .models import Ratting,Comment

class RattingAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'created_date', 'modified_date']
    list_filter = ['created_date', 'modified_date']
    search_fields = ['user__username', 'product__product_name']

admin.site.register(Ratting, RattingAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'comment', 'created_date', 'modified_date']
    list_filter = ['created_date', 'modified_date']
    search_fields = ['user__username', 'product__product_name']

admin.site.register(Comment, CommentAdmin)
