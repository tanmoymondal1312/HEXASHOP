from django import forms
from store.models import Product
from category.models import Category

class ProductForm(forms.ModelForm):
    # Add a custom category field to display choices from the Category model
    category = forms.ModelChoiceField(
        
        queryset=Category.objects.all(),
        empty_label="None",  # Set the empty label to "None" or any other value you prefer
        required=True,  # Set to False to make the field optional
        widget=forms.Select(attrs={'class': 'custom-select'}),  # Add CSS class
    )
    color = forms.ChoiceField(choices=Product.COLOR_CHOICES, required=True)
    sizes = forms.ChoiceField(choices=Product.SIZE_CHOICES, required=True)

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
            'sizes',
            'color',
            'category',
        ]

    # Add any additional form field customizations or validation here
    def clean_price(self):
        # Example: Custom validation for the 'price' field
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price



