from django.urls import path
from . import views

urlpatterns = [
    # Add other URL patterns for your app here if needed

    # URL pattern for creating a seller
    path('create_seller/', views.create_seller, name='create_seller'),
    path('enter_confirmation_code/', views.enter_confirmation_code, name='enter_confirmation_code'),

    # Add more URL patterns as necessary
]


