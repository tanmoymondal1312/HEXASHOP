from django import forms
from .models import Reviews


class MyForm(forms.Form):
    field1 = forms.IntegerField(label='Field 1')
    field2 = forms.IntegerField(label='Field 2')
    field3 = forms.ChoiceField(label='Field 3', choices=[
        ('None', 'All Sizes'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', '2 x Extra Large'),
        ('XXXL', '3 x Extra Large'),
    ])
    field4 = forms.ChoiceField(label='Field 4', choices=[
    ('Red', 'Red'),
    ('White','White'),
    ('Blue', 'Blue'),
    ('Green', 'Green'),
    ('Yellow', 'Yellow'),
    ('Black', 'Black'),
    
])

class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['comment', 'rating']

    comment = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
    )

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating is not None and (rating < 1 or rating > 5):
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating
