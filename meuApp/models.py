from django.db import models
from django.utils import timezone


# Create your models here.

class Episode(models.Model):
    name = models.CharField(max_length=150, null=False)
    air_date = models.CharField(max_length=50, null=True, blank=False)
    episode = models.CharField(max_length=50, null=True, blank=False)
    
    
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=150, null=False)
    type = models.CharField(max_length=50, null=True, blank=False)
    dimension = models.CharField(max_length=50, null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=150, null=False)
    status = models.CharField(max_length=50, null=True, blank=False)
    species = models.CharField(max_length=50, null=True, blank=False)
    type = models.CharField(max_length=50, null=True, blank=False)
    gender = models.CharField(max_length=50, null=True)
    origin = models.CharField(max_length=50, null=True)
    location = models.ForeignKey(Location, related_name="location", on_delete=models.CASCADE) # foreign key
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
