from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProfileSettings, name='profile_settings'),
    #path('upload_profile/', views.upload_profile_picture, name='upload_user_profile_picture'),
]