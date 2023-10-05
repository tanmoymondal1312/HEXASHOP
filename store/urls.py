from django.urls import path
from . import views  # Import your views module here

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='store_by_category'),
    #path('filteritems/', views.FilterItems, name='filter_items'),
    path('feature-not-availabe-for-delopers-developing-/',views.FeatureNV, name='featurenv')
    
]
