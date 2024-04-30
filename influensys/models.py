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
    industry = ArrayField(models.CharField(max_length=255), blank=True)   # industry based filter
    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=255, blank=True, null=True)
    annual_revenue = models.FloatField(blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)


class TargetInfo(models.Model):
    influencer = models.ForeignKey(Influencers, on_delete=models.CASCADE)
    objectives = models.TextField(blank=True, null=True)
    target_age = ArrayField(models.CharField(max_length=255), blank=True)
    country = models.JSONField(blank=True, null=True)
    target_gender = ArrayField(models.CharField(max_length=255), blank=True)
    target_income_level = ArrayField(models.CharField(max_length=255), blank=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    communication_channel = models.CharField(max_length=255, blank=True, null=True)
    selected_interests = ArrayField(models.CharField(max_length=255))


class InfluencerInstagramTokens(models.Model):
    influencer = models.ForeignKey(Influencers, models.CASCADE)
    token = models.CharField(max_length=1000)
