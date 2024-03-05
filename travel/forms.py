from django import forms
from django.contrib.auth.models import User
from .models import Account, Place, Booking, Trip, Review

class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('user', 'name', 'phone_no', 'image')

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