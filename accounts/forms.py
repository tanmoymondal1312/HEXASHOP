from django import forms
from .models import CustomUser
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Replace 'User' with your user model if needed
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)