from django.contrib import admin

# Register your models here.
from .models import Account, Place, Booking, Trip, Review

admin.site.register(Account)
admin.site.register(Place)
admin.site.register(Booking)
admin.site.register(Trip)
admin.site.register(Review)