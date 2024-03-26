from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods

from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from .models import UserProfile

@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect(home)

    else:
        form = UserRegistrationForm()

    return render(request, 'travel/login_register.html', {"form": form})

@require_http_methods(["GET", "POST"])
def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('travel/index.html')
            else:
                messages.error(request, "Invalid email or password.")

    else:
        form = UserLoginForm()

    return render(request, 'travel/index.html' , {"form": form})

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

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
    return redirect('travel/login_register.html')

def trip(request):
    return render(request, 'travel/trip.html')
# Create your views here.
def home(request):
    return render(request, 'travel/index.html')