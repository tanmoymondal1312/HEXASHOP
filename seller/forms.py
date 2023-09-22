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
    def clean_email(self):
        email = self.cleaned_data['email']
        # Check if an instance with the same email already exists in the database
        if Seller.objects.filter(email=email).exists():
            raise forms.ValidationError("𝑻𝒉𝒊𝒔 𝒆𝒎𝒂𝒊𝒍 𝒂𝒅𝒅𝒓𝒆𝒔𝒔 𝒊𝒔 𝒂𝒍𝒓𝒆𝒂𝒅𝒚 𝒊𝒏 𝒖𝒔𝒆.")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        profile_picture = cleaned_data.get('profile_picture')

        if not profile_picture:
            print("Under if")
            raise forms.ValidationError("𝒀𝒐𝒖 𝒅𝒊𝒅 𝒏𝒐𝒕 𝒔𝒖𝒃𝒎𝒊𝒕 𝒚𝒐𝒖𝒓 𝒑𝒊𝒄𝒕𝒖𝒓𝒆.")
          


class ConfirmationCodeForm(forms.Form):
    confirmation_code = forms.CharField(
        label='Confirmation Code',
        max_length=6,  # Assuming your confirmation code is 6 digits long
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
