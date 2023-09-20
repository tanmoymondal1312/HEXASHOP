from django import forms
from accounts.models import CustomUser

class UserProfilePictureForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [            
            'user_profile_picture',
        ]