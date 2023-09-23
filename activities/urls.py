from django.urls import path
from . import views

urlpatterns = [
    path('', views.ActivitiesHome, name='activities_home'),

]


