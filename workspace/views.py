from django.shortcuts import render
from store.models import Product


def Home(request):
    return render(request, 'home.html')



