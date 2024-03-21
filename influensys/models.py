from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

INDUSTRY_TYPES = (())


class Influencers(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    industry = models.CharField(max_length=255, choices=INDUSTRY_TYPES)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    annual_revenue = models.FloatField()
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
