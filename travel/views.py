from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from django.contrib import messages
from .models import *


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please login.')
            return redirect('home')  # Redirect to the homepage after successful registration
        else:
            messages.error(request, 'Registration failed. Please check the form data.')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'travel/index.html')

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        form = UserProfileForm(
            request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")

    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'travel/index.html', {"form": form})


@login_required
def log_out(request):
    logout(request)
    messages.success(request, "Logout successful!")
    return redirect('home')


@login_required
def trip(request):
    return render(request, 'travel/trip.html')


def navbar(request):
    return render(request, 'travel/navbar.html')
# Create your views here.


def home(request):
    return render(request, 'travel/index.html')
