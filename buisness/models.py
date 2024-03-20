from django.conf import settings
from django.db import models

INDUSTRY_TYPES = (())


class Businesses(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    crn = models.CharField(max_length=255)
    industry = models.CharField(max_length=255, choices=INDUSTRY_TYPES)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    description = models.TextField()
    annual_revenue = models.DecimalField(max_digits=2)
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
