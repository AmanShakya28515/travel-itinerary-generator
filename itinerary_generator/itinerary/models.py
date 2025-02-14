from django.db import models
from django.contrib.auth.models import User


class TravelPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=200)
    current_destination = models.CharField(max_length=200, null=True, blank=True)  # New field for the current destination
    start_date = models.DateField()
    end_date = models.DateField()
    budget_category = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Mid', 'Mid'), ('High', 'High')])
    itinerary_generated = models.BooleanField(default=False)  # To indicate if itinerary is generated
    weather_info = models.JSONField(null=True, blank=True)  # To store weather details

    def __str__(self):
        return f"Travel Plan for {self.user.username} to {self.destination}"


class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    district = models.ForeignKey(District, related_name='hotels', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    budget_category = models.CharField(max_length=50)
    price_range = models.CharField(max_length=50)
    hotel_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.district.name})"

class Activity(models.Model):
    district = models.ForeignKey(District, related_name='activities', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name} - {self.district.name} ({self.category})"

