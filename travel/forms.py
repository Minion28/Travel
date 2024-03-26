from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ("email", "password")

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
