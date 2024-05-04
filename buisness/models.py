from django.conf import settings
from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from influensys.models import *

CONFIRMATIONS = (('Pending', 'Pending'),
                 ('Rejected', 'Rejected'),
                 ('Confirmed', 'Confirmed'))


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
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    slug = models.CharField(max_length=100, unique=True)


class BusinessGoals(models.Model):
    business = models.ForeignKey(Businesses, on_delete=models.CASCADE, related_name='business_goals')
    objectives = models.TextField(blank=True, null=True)
    budget = models.CharField(max_length=255, blank=True, null=True)
    age = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    kpi = models.CharField(max_length=255, blank=True, null=True)
    country = models.JSONField(blank=True, null=True)
    gender = ArrayField(models.CharField(max_length=255), blank=True)
    address = models.TextField(blank=True, null=True)
    income_level = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    communication_channel = models.CharField(max_length=255, blank=True, null=True)
    selected_interests = ArrayField(models.CharField(max_length=255))

    def __str__(self):
        return f"Survey Objectives: {self.objectives}"


class Events(models.Model):
    business = models.ForeignKey(Businesses, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)  #
    description = models.TextField(blank=True, null=True)  #
    event_type = ArrayField(models.CharField(max_length=255), blank=True)
    start_date = models.DateField(blank=True, null=True)  #
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    # duration = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)  #
    goals = models.TextField(blank=True, null=True)
    target_age = models.CharField(max_length=255, blank=True, null=True)
    target_gender = models.CharField(max_length=255, blank=True, null=True)
    target_income = models.CharField(max_length=255, blank=True, null=True)
    communication_channel = models.CharField(max_length=255, blank=True, null=True)
    target_interests = ArrayField(models.CharField(max_length=255))
    target_occupation = models.CharField(max_length=255, blank=True, null=True)
    budget = models.CharField(max_length=255, blank=True, null=True)


class Campaigns(models.Model):
    business = models.ForeignKey(Businesses, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    channel_section = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    budget = models.CharField(max_length=255, blank=True, null=True)
    remaining_budget = models.CharField(max_length=255, blank=True, null=True)
    creative_asset = models.CharField(max_length=255, blank=True, null=True)
    breakdown = models.CharField(max_length=255, blank=True, null=True)
    target_age = models.CharField(max_length=255, blank=True, null=True)
    target_gender = ArrayField(models.CharField(max_length=255))
    target_income_level = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    interests = ArrayField(models.CharField(max_length=255))
    communication_channel = models.CharField(max_length=255)
    content_formats = models.CharField(max_length=255, blank=True, null=True)
    distribution_channels = models.CharField(max_length=255, blank=True, null=True)
    offer_description = models.CharField(max_length=255, blank=True, null=True)
    offer_terms = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)


STATUS = (('Pending', 'Pending'),
          ('Approved', 'Approved'),
          ('Rejected', 'Rejected'))


class CampaignInfluencers(models.Model):
    business = models.ForeignKey(Businesses, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaigns, on_delete=models.CASCADE)
    influencer = models.ForeignKey(Influencers, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    status = models.CharField(max_length=255, choices=STATUS, default='Pending')
    cost = models.CharField(max_length=255, blank=True, null=True)
    transaction_id = models.TextField(blank=True, null=True)


class InfluencerWork(models.Model):
    campaign = models.ForeignKey(Campaigns, on_delete=models.CASCADE)
    influencer = models.ForeignKey(Influencers, on_delete=models.CASCADE)
    video = models.URLField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    marketer_response = models.TextField(blank=True, null=True)
    confirmation = models.CharField(max_length=255, choices=CONFIRMATIONS, default='Pending', blank=True, null=True)



class EventInfluencer(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    influencer = models.ForeignKey(Influencers, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    status = models.CharField(max_length=255, choices=STATUS, default='Pending')
    message = models.TextField(blank=True, null=True)


class Products(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    specification = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    business = models.ForeignKey(Businesses, on_delete=models.CASCADE)


class Gifts(models.Model):
    product = models.ManyToManyField(Products)
    influencer = models.ForeignKey(Influencers, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    confirmation = models.CharField(max_length=255, choices=CONFIRMATIONS, default='Pending', blank=True, null=True)
    amount = models.CharField(max_length=255, blank=True, null=True)
    business = models.ForeignKey(Businesses, on_delete=models.CASCADE)


class YoutubeInsights(models.Model):
    insight = models.JSONField(null=True, blank=True)
    business = models.ForeignKey(Businesses, on_delete=models.CASCADE)


class InfluencerInsights(models.Model):
    insight = models.JSONField(null=True, blank=True)
    influencer = models.ForeignKey(Influencers, on_delete=models.CASCADE)
