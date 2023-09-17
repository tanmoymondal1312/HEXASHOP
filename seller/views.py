from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Seller
from .forms import SellerForm  # You will need to create a SellerForm for editing the seller profile

@login_required
def create_seller(request):
    user = request.user
    seller_profile, created = Seller.objects.get_or_create(user=user)
    

    if request.method == 'POST':
        form = SellerForm(request.POST, request.FILES,  instance=seller_profile)
        if form.is_valid():
            
            form.save()
            user.is_seller = True
            user.save()
            return redirect('profile_settings')  # Redirect to the seller profile page after saving
    else:
        form = SellerForm

    context = {
        'form': form,
    }

    return render(request, 'create_seller.html', context)
