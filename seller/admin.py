from django.contrib import admin
from .models import Seller  # Import the Seller model from your app's models

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    # List of fields to display in the admin list view for Seller objects
    list_display = ('name', 'email')

# You can customize the SellerAdmin class further if needed.
