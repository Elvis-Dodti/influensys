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
    business = BuisnessSerializer(read_only=True)

    class Meta:
        model = Events
        fields = [
            "id",
            "business",
            "name",
            "description",
            "objective",
            "event_type",
            "date",
            "time",
            "duration",
            "location"
        ]


class CampaignSerializer(serializers.ModelSerializer):
    business = BuisnessSerializer(read_only=True)

    class Meta:
        model = Campaigns
        fields = [
            "id",
            "business",
            "name",
            "description",
            "objective",
            "channel_section",
            "start_date",
            "end_date",
            "duration",
            "budget"
        ]
