from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import *


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            raise ValidationError("Invalid username or password.")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("name", "image", "phone_number")

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('image', 'title', 'topic', 'description', 'link_to_more_images')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('trip_location', 'seat_number')

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ('location', 'price', 'number_of_seats')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review',)

class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
