from django.urls import path
from . import views

app_name = 'message'

urlpatterns = [
    path('send/<int:receiver_id>/', views.send_message, name='send_message'),
    path('list/', views.message_list, name='message_list'),
]
