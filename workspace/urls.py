from django.urls import path
from . import views

urlpatterns = [
    # Add other URL patterns for your app here if needed

    # URL pattern for creating a seller
    path('', views.Home, name='work_space_home'),
    path('upload_products/', views.UploadProduct, name='upload_products'),
    # Add more URL patterns as necessary
]


