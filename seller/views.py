from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from accounts.models import CustomUser
from .models import Seller
from .forms import SellerForm,ConfirmationCodeForm
from django.contrib import messages
from django.core.mail import EmailMessage
from activities.models import Activities
import re

import random


def generate_confirmation_code():
    # Generate a 6-digit random number
    confirmation_code = ''.join(random.choice('0123456789') for _ in range(6))
    return confirmation_code


# views.py

# ... (import statements)




from .models import Seller  # Import the Seller model

@login_required
def create_seller(request):
    form = SellerForm()
    
    try:
        seller = Seller.objects.get(user=request.user)
        if seller.user.is_seller:
            messages.error(request, 'You are already a seller')
            return redirect('profile_settings')
    except Seller.DoesNotExist:
        seller = None
    
    if request.method == 'POST':
        form = SellerForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            # Check if a seller with the given email exists
            existing_seller = Seller.objects.filter(email=email).first()
            
            if existing_seller:
                # Email exists in Seller model, redirect to profile_settings
                return redirect('create_seller')
            else:
                confirmation_code = generate_confirmation_code()
                
                # Create a new Seller object without associating it with any user
                new_seller = Seller(
                    user=request.user,
                    name=form.cleaned_data['name'],
                    profile_picture=form.cleaned_data['profile_picture'],
                    phone_number=form.cleaned_data['phone_number'],
                    email=email,
                    company_name=form.cleaned_data['company_name'],
                    website=form.cleaned_data['website'],
                    date_of_birth=form.cleaned_data['date_of_birth'],
                    country=form.cleaned_data['country'],
                    division=form.cleaned_data['division'],
                    district=form.cleaned_data['district'],
                    confirmation_code=confirmation_code
                )
                
                new_seller.save()
                
                # Send the confirmation email
                mail_subject = 'HEXASHOP SELLER VERIFICATION CODE'
                message = f'Your verification code is: {confirmation_code}'
                to_email = email
                send_email = EmailMessage(mail_subject, message, to=[to_email])
                send_email.send()
                
                return redirect('enter_confirmation_code')
    
    return render(request, 'create_seller.html', {'form': form})



from django.db import transaction

@login_required
def enter_confirmation_code(request):
    try:
        seller = Seller.objects.get(user=request.user)
        if seller.user.is_seller:
            messages.error(request, 'You are already a seller, do not try again to access this page')
            return redirect('profile_settings')
    except Seller.DoesNotExist:
        seller = None
        messages.error(request, 'Please register as a seller first.')
        activities_instance = Activities(data=f"You request for a seller (Not excepted)",user=request.user)
        activities_instance.save()
        return redirect('create_seller')
    form = ConfirmationCodeForm()
    if request.method == 'POST':
        confirmation_code = request.POST.get('confirmation_code')
        user = request.user
        
        if re.search(r'\D', confirmation_code):
            messages.error(request, '𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗰𝗼𝗱𝗲. 𝗣𝗹𝗲𝗮𝘀𝗲 𝘁𝗿𝘆 𝗮𝗴𝗮𝗶𝗻.')
            return redirect('enter_confirmation_code')
            
        
        try:
            email = request.user.seller_profile.email
            user = request.user
            matching_seller = Seller.objects.get(user__seller_profile__email=email)      
            mafc = int(confirmation_code)
            
            
            madb = matching_seller.confirmation_code
            
            if mafc == madb:
                matching_seller.user.is_seller = True
                matching_seller.is_seller = True
                matching_seller.user.save()
                matching_seller.save()
                
                activities_instance = Activities(data=f"You joind HEXASHOP as a seller at",user=request.user)
                activities_instance.save()
                
                return redirect('profile_settings')
            else:
                messages.error(request, '𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗰𝗼𝗱𝗲. 𝗣𝗹𝗲𝗮𝘀𝗲 𝘁𝗿𝘆 𝗮𝗴𝗮𝗶𝗻.')
                return redirect('enter_confirmation_code')
        except Seller.DoesNotExist:
            messages.error(request, 'Confirmation code not found.')
            
    

    return render(request, 'enter_confirmation_code.html', {'form': form})
