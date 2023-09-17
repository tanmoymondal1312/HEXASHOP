from django import forms
from .models import Seller

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = [
            'name',
            'profile_picture',
            'phone_number',
            'email',
            'company_name',
            'website',
            'date_of_birth',
            'country',
            'division',
            'district',
        ]
