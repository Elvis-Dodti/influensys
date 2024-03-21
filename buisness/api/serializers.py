from rest_framework import serializers
from buisness.models import *


class BuisnessSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Businesses
        fields = ['id', 'user', 'name', 'crn', 'industry', 'address',
                  'country', 'pincode', 'description',
                  'annual_revenue', 'facebook', 'instagram', 'website', 'slug']
class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = '__all__'