from django import forms
from .models import Reviews


class MyForm(forms.Form):
    
    field1 = forms.IntegerField(label='Field 1')
    field2 = forms.IntegerField(label='Field 2')
    


class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Reviews 
        fields = ['comment','rating'] 

    comment = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
    )
