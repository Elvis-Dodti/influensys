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
    slug = models.CharField(max_length=100, unique=True)


EVENT_TYPE = (())


class Events(models.Model):
    business = models.ForeignKey(Businesses, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    objective = models.TextField()
    event_type = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()
    location = models.CharField(max_length=255)
