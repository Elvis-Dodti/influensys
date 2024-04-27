from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InfluensysInfluencers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    industry = models.TextField()  # This field type is a guess.
    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=255, blank=True, null=True)
    annual_revenue = models.FloatField(blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(User, models.DO_NOTHING)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'influensys_influencers'