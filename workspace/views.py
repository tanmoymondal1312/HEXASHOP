from django.shortcuts import render
from store.models import Product
from django.shortcuts import render, redirect
from .forms import ProductForm
from category.models import Category
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import CustomUser
from django.shortcuts import render, redirect, get_object_or_404



def Home(request):
    return render(request, 'home.html')



def UploadProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a Product instance and set the created_by field to the current user
            product = form.save(commit=False)
            product.created_by = request.user.seller_profile  # Access the currently authenticated user
            product.save()
            return redirect('work_space_home')  # Redirect to a success page or product list
    else:
        form = ProductForm(initial={'is_available': True})
    categories = Category.objects.all()

    return render(request, 'upload_products.html', {'form': form, 'categories': categories})



