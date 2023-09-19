from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from accounts.models import CustomUser
from .models import Seller
from .forms import SellerForm,ConfirmationCodeForm
from django.contrib import messages
from django.core.mail import EmailMessage

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
    try:
        seller = Seller.objects.get(user=request.user)
        if seller.user.is_seller:
            messages.error(request, 'You are already a seller')
            return redirect('profile_settings')
    except Seller.DoesNotExist:
        seller = None
        print(seller)
        if request.method == 'POST':
            form = SellerForm(request.POST, request.FILES)
            user = request.user

            if form.is_valid():
                email = form.cleaned_data['email']
                confirmation_code = generate_confirmation_code()

                mail_subject = 'HEXASHOP for seller'
                message = f'Your verification code is: {confirmation_code}'
                to_email = email
                send_email = EmailMessage(mail_subject, message, to=[to_email])
                send_email.send()

                # Create a new Seller object without associating it with any user
                seller = Seller.objects.create(
                    user=user,
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

                form.save()

                return redirect('enter_confirmation_code')

        else:
            form = SellerForm()

        context = {
            'form': form,
        }
        
    return render(request, 'create_seller.html', context)



from django.shortcuts import get_object_or_404

@login_required
def enter_confirmation_code(request):
    try:
        seller = Seller.objects.get(user=request.user)
        if seller.user.is_seller:
            messages.error(request, 'You are already a seller do not  try again to access those page')
            return redirect('profile_settings')
    except Seller.DoesNotExist:
        seller = None
    form = ConfirmationCodeForm()  # Move the form declaration to the beginning of the view function
    
    if request.method == 'POST':
        
        confirmation_code = request.POST.get('confirmation_code')
        user = request.user
        #print(confirmation_code)
        try:
            matching_seller = Seller.objects.get(confirmation_code=confirmation_code)
            
            #print(matching_seller)           
            #print(matching_seller.confirmation_code)           
            #print(confirmation_code)
            
            mafc = int(confirmation_code)
            
            madb = matching_seller.confirmation_code
            

            if mafc == madb:
                matching_seller.user.is_seller = True
                matching_seller.is_seller =True
                matching_seller.user.save()  # Save the user to update the 'is_seller' attribute
                matching_seller.save()
                
                return redirect('profile_settings')
                
                
            else:
                messages.error(request, 'Invalid confirmation code. Please try again.')
                #print('Invalid confirmation code. Please try again')
        except Seller.DoesNotExist:
            messages.error(request, 'Confirmation code not found.')
            matching_seller.delete()
            #print('Confirmation code not found')

    context = {
        'form': form,
    }

    return render(request, 'enter_confirmation_code.html', context)


#Private routing