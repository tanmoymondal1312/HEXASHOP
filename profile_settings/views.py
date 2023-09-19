from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from seller.models import Seller

# Create your views here.
@login_required  # This decorator ensures that the user is logged in to access this view
def ProfileSettings(request):
    # Retrieve the user's data from the request object
    user_id = request.user.id
    user = CustomUser.objects.get(id=user_id)
    
    try:
        seller_profile = user.seller_profile
    except:
        seller_profile = None

    # You can access the user's attributes such as username, email, first_name, and last_name
    username = user.username
    email = user.email
    first_name = user.first_name
    last_name = user.last_name
    is_seller = user.is_seller
    try:
        is_seller_seller = seller_profile.is_seller
    except:
        
        is_seller_seller = None

    # Create a context dictionary to pass data to the template
    context = {
        'username': username,
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'is_seller': is_seller,
        'is_seller_seller':is_seller_seller
    }

    # Render a template with the user's data
    return render(request, 'profile_settings.html', context)
