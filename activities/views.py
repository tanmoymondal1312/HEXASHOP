from django.shortcuts import render

# Create your views here.


def ActivitiesHome(request):
    return render(request, 'activities_home.html')