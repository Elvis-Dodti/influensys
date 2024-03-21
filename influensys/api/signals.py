import random
import string
from django.db.models.signals import pre_save, pre_delete, post_delete
from django.dispatch import receiver
from django.utils.text import slugify
from influensys.models import *


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


@receiver(pre_save, sender=Influencers)
def add_slug_to_influencer(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.name)
        random_string = rand_slug()
        instance.slug = f"{slug}-{random_string}"
