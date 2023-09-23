from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'slug',
            'description',
            'price',
            'image',
            'stock',
            'is_available',
            'category',
            'sizes',
            'color',
        ]

    # You can add additional validation or customization here if needed.
