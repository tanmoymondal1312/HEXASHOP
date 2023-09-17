from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser

# Create your views here.
@login_required  # This decorator ensures that the user is logged in to access this view
def ProfileSettings(request):
    # Retrieve the user's data from the request object
    user_id = request.user.id
    user = CustomUser.objects.get(id=user_id)

    # You can access the user's attributes such as username, email, first_name, and last_name
    username = user.username
    email = user.email
    first_name = user.first_name
    last_name = user.last_name
    is_seller = user.is_seller

    # Create a context dictionary to pass data to the template
    context = {
        'username': username,
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'is_seller': is_seller,
    }

    # Render a template with the user's data
    return render(request, 'profile_settings.html', context)
