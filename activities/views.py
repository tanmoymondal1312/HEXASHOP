from django.shortcuts import render
from .models import Activities

def ActivitiesHome(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Filter activities for the current user
        activities = Activities.objects.filter(user=request.user).order_by('-created_date')
        context = {'activities': activities}
        return render(request, 'activities_home.html', context)
    else:
        # Handle the case where the user is not authenticated
        return render(request, 'not_authenticated.html')
