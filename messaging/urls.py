from django.urls import path
from . import views

urlpatterns = [
    path('chat/<int:receiver_id>/', views.chat, name='chat'),
    path('get_messages/<int:receiver_id>/', views.get_messages, name='get_messages'),
]
