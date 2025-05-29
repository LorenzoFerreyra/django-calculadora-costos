from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.TextField()

    def __str__(self):
        return self.location
    
class Food(models.Model):
    food = models.TextField()
    water = models.TextField()

    def __str__(self):
        return self.food
    
    
class Transport(models.Model):
    transport = models.TextField()

    def __str__(self):
        return self.transport