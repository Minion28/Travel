from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import *


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please login.')
            return redirect('home')
        else:
            form.errors
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/login.html', {'form': form})


def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active and not user.is_staff:
                    login(request, user)
                    return redirect('home')
                else:
                    form.errors  # Change 'home' to your desired URL
            else:
                form.errors
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def custom_logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


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


def home(request):
    return render(request, 'travel/index.html')
