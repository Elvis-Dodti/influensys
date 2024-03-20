from rest_framework import serializers
from buisness.models import *


class BuisnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Businesses
        fields = '__all__'
class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = '__all__'