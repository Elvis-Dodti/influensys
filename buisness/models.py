from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Businesses(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    crn = models.CharField(max_length=255)
    industry = ArrayField(models.CharField(max_length=255))
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    description = models.TextField()
    annual_revenue = models.FloatField()
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    slug = models.CharField(max_length=100, unique=True)


class Events(models.Model):
    business = models.ForeignKey(Businesses, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    objective = models.TextField()
    event_type = ArrayField(models.CharField(max_length=255))
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()
    location = models.CharField(max_length=255)


class Campaigns(models.Model):
    buisness = models.ForeignKey(Businesses, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    objective = models.TextField()
    channel_section = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.DurationField()
    budget = models.FloatField()
