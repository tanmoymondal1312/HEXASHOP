from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from seller.models import Seller
from .forms import UserProfilePictureForm
from django.contrib import messages
from activities.models import Activities

@login_required
def ProfileSettings(request):
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
    profile_picture = user.user_profile_picture
    try:
        is_seller_seller = seller_profile.is_seller
    except:
        is_seller_seller = None

    if request.method == 'POST':
        form = UserProfilePictureForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            activities_instance = Activities(data=f"You update your picture on",user=request.user)
            activities_instance.save()
            messages.success(request, 'Profile picture updated successfully.')
            return redirect('profile_settings')  # Redirect to the user's profile page after a successful upload
    else:
        form = UserProfilePictureForm(instance=user)

    # Create a context dictionary to pass data to the template
    context = {
        'username': username,
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'is_seller': is_seller,
        'profile_picture': profile_picture,
        'is_seller_seller': is_seller_seller,
        
        'form': form,  # Include the form in the context
    }

    # Render a template with the user's data and the profile picture upload form
    return render(request, 'profile_settings.html', context)
