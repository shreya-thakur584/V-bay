from django.db import models

class UserRegistration(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=128)
    mobile_number = models.CharField(max_length=15)