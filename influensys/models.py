from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import ArrayField

INDUSTRY_TYPES = (())


class Influencers(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    industry = ArrayField(models.CharField(max_length=255), blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=255, blank=True, null=True)
    annual_revenue = models.FloatField(blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=100, unique=True)


# class TargetInfo(models.Model):
#     influencers = models.ForeignKey(Influencers, on_delete=models.CASCADE)
#     audience_age = models.CharField(max_length=255)
#     audience_gender = models.CharField(max_length=255)
#     tags = ArrayField(models.CharField(max_length=255))


