from django import forms


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
    ('None', 'All Color'),
    ('Red', 'Red'),
    ('White','White'),
    ('Blue', 'Blue'),
    ('Green', 'Green'),
    ('Yellow', 'Yellow'),
    ('Black', 'Black'),
    ('Violet', 'Violet'),
    
])




# class MyForm(forms.Form):
#     field1 = forms.IntegerField(label='Field 1')
#     field2 = forms.IntegerField(label='Field 2')
#     field3 = forms.ChoiceField(label='Field 3', choices=[
#         ('None', 'All Sizes'),
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#         ('XL', 'Extra Large'),
#         ('XXL', '2 x Extra Large'),
#         ('XXXL', '3 x Extra Large'),
#     ])
#     field4 = forms.ChoiceField(label='Field 4', choices=[
#     ('None', 'All Color'),
#     ('Red', 'Red'),
#     ('White','White'),
#     ('Blue', 'Blue'),
#     ('Green', 'Green'),
#     ('Yellow', 'Yellow'),
#     ('Black', 'Black'),
#     ('Violet', 'Violet'),
    
# ])
