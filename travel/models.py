from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profile_images/", blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username

class Place(models.Model):
    image = models.ImageField(upload_to='places/')
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    description = models.TextField()
    link_to_more_images = models.URLField()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip_location = models.ForeignKey('Trip', on_delete=models.CASCADE)
    seat_number = models.IntegerField()

class Trip(models.Model):
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    number_of_seats = models.IntegerField()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()