from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Type your message here...'}))
    
    class Meta:
        model = Message
        fields = ['content']