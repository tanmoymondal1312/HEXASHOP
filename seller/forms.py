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

class ConfirmationCodeForm(forms.Form):
    confirmation_code = forms.CharField(
        label='Confirmation Code',
        max_length=6,  # Assuming your confirmation code is 6 digits long
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
