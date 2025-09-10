from django.db import models

# Create your models here.
class Contact(models.Model):
    First_Name = models.CharField(max_length=125)
    Last_Name = models.CharField(max_length=125)
    Email = models.CharField(max_length=125)
    PhoneNumber = models.CharField(max_length=12)
    City = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('P', 'Princess'),
        ('O', 'Other'),
    ]
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Goals = models.TextField(max_length=125)
    
