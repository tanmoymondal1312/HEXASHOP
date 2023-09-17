from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from .forms import SignupForm, LoginForm  # Import your SignupForm and LoginForm
from .models import CustomUser
from cart.models import Cart, CartItem
from cart.views import _cart_id
import logging  # Import the logging module

# Configure the logger
logger = logging.getLogger(__name__)

def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        password1 = form.data.get('password1')
        password2 = form.data.get('password2')
        if password1 == password2:
            if form.is_valid():
                try:
                    # Check password strength
                    try:
                        validate_password(password1)
                    except DjangoValidationError as e:
                        form.add_error('password1', e)
                        return render(request, 'accounts/register.html', {'form': form})

                    user = form.save()  # Save the user with form data
                    login(request, user)
                    return redirect('home')
                except IntegrityError:
                    form.add_error('username', 'Username has already been taken')
                    logger.error('IntegrityError: Duplicate username during registration')
            else:
                # Form is not valid due to other reasons
                return render(request, 'accounts/register.html', {'form': form})
        else:
            form.add_error('password2', 'Try Same password in the two fields')
    else:
        form = SignupForm()
    return render(request, 'accounts/register.html', {'form': form})

def profile(request):
    return render(request, 'accounts/dashboard.html')

def user_login(request):
    form = LoginForm()  # Create an instance of the login form

    if request.method == 'POST':
        form = LoginForm(request.POST)  # Bind the form to the POST data
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                try:
                    cart = Cart.objects.get(cart_id=_cart_id(request))
                    is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                    if is_cart_item_exists:
                        cart_item = CartItem.objects.filter(cart=cart)
                        for item in cart_item:
                            item.user = user
                            item.save()
                except Exception as e:
                    logger.error(f"Error during cart item migration: {e}")
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid login credentials')
                logger.error('Invalid login credentials')
                return redirect('login')

    return render(request, 'accounts/signin.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
