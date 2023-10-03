from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from.models import Ratting

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Ratting
from .serializers import RattingSerializer
from rest_framework import generics

# Create your views here.
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    ratings = Ratting.objects.filter(product=product)
    
    # Calculate the average rating
    total_ratings = ratings.count()
    if total_ratings > 0:
        average_rating = round(sum(rating.rating for rating in ratings) / total_ratings, 1)
    else:
        average_rating = 0.0
    
    return render(request, 'product_detail.html', {'product': product, 'average_rating': average_rating})





class RattingCreateAPIView(generics.CreateAPIView):
    queryset = Ratting.objects.all()
    serializer_class = RattingSerializer

