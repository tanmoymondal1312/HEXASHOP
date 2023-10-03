from django.urls import path
from . import views  

urlpatterns = [
    
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('api/ratting/create/', views.RattingCreateAPIView.as_view(), name='ratting-create'),
    
]



    