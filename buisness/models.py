from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Businesses(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    crn = models.CharField(max_length=255, blank=True, null=True)
    industry = ArrayField(models.CharField(max_length=255), blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    annual_revenue = models.FloatField(blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    # image = models.ImageField(upload_to='media/', blank=True, null=True)
    slug = models.CharField(max_length=100, unique=True)


class BusinessGoals(models.Model):
    business = models.ForeignKey(Businesses, on_delete=models.CASCADE, related_name='business_goals')
    objectives = models.TextField(blank=True, null=True)
    budget = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    kpi = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    gender = ArrayField(models.CharField(max_length=255), blank=True)
    address = models.TextField(blank=True, null=True)
    income_level = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    communication_channel = models.CharField(max_length=255, blank=True, null=True)
    selected_interests = ArrayField(models.CharField(max_length=255))

    def __str__(self):
        return f"Survey Objectives: {self.objectives}"


class Events(models.Model):
    business = models.ForeignKey(Businesses, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    event_type = ArrayField(models.CharField(max_length=255))
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)


class Campaigns(models.Model):
    business = models.ForeignKey(Businesses, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    channel_section = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    budget = models.CharField(max_length=255, blank=True, null=True)
    creative_asset = models.CharField(max_length=255, blank=True, null=True)
    breakdown = models.CharField(max_length=255, blank=True, null=True)
    target_age = models.CharField(max_length=255, blank=True, null=True)
    target_gender = ArrayField(models.CharField(max_length=255))
    target_income_level = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    interests = ArrayField(models.CharField(max_length=255))
    communication_channel = models.CharField(max_length=255, blank=True, null=True)
    content_formats = models.CharField(max_length=255, blank=True, null=True)
    distribution_channels = models.CharField(max_length=255, blank=True, null=True)
    offer_description = models.CharField(max_length=255, blank=True, null=True)
    offer_terms = models.CharField(max_length=255, blank=True, null=True)



