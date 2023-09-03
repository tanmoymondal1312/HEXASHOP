from django.urls import path
from . import views  # Import your views module here

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='store_by_category'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'), 
    path('filteritems/', views.FilterItems, name='filter_items')
]
