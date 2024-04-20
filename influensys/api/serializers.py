from rest_framework import serializers

from buisness.api.serializers import BuisnessSerializer
from influensys.models import *
from buisness.models import *
from buisness.api.serializers import *


class InfluencerSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Influencers
        fields = [
            "id",
            "user",
            "name",
            "description",
            "email",
            "phone",
            "industry",
            "address",
            "country",
            "pincode",
            "annual_revenue",
            "facebook",
            "instagram",
            "website",
            "slug"
        ]


class TargetInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetInfo
        fields = [
            "influencer",
            "objectives",
            "target_age",
            "country",
            "target_gender",
            "target_income_level",
            "occupation",
            "communication_channel",
            "selected_interests"
        ]
        read_only_fields = ["influencer"]


class EventInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'name', 'description', 'start_date',
                  'country']


class EventOptInSerializer(serializers.ModelSerializer):
    event = EventInfoSerializer(read_only=True)

    class Meta:
        model = EventInfluencer
        fields = ['id', 'event', 'influencer', 'confirmed']


class CampaignOptSerializer(serializers.ModelSerializer):
    business = BuisnessSerializer(read_only=True)
    campaign = CampaignSerializer(read_only=True)

    class Meta:
        model = CampaignInfluencers
        fields = ['id', 'business', 'campaign', 'influencer',
                  'confirmed']
