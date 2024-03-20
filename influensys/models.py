from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Influencers(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


