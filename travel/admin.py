from django.contrib import admin

# Register your models here.
from .models import UserProfile, Place, Booking, Trip, Review

admin.site.register(UserProfile)
admin.site.register(Place)
admin.site.register(Booking)
admin.site.register(Trip)
admin.site.register(Review)