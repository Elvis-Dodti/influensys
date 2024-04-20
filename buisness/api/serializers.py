from rest_framework import serializers
from buisness.models import *


class BuisnessSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Businesses
        fields = [
            "id",
            "user",
            "name",
            "crn",
            "industry",
            "address",
            "country",
            "pincode",
            "description",
            "annual_revenue",
            "facebook",
            "instagram",
            "website",
            "phone",
            "email",
            "slug"
        ]


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


class BusinessGoalsSerializer(serializers.ModelSerializer):
    business = serializers.StringRelatedField(read_only=True, source='business.id')

    class Meta:
        model = BusinessGoals
        fields = [
            "id",
            "business",
            "objectives",
            "budget",
            "age",
            "kpi",
            "country",
            "gender",
            "address",
            "income_level",
            "occupation",
            "communication_channel",
            "selected_interests"
        ]


class EventSerializer(serializers.ModelSerializer):
    business = serializers.StringRelatedField(read_only=True, source='business.id')

    class Meta:
        model = Events
        fields = [
            "id",
            "business",
            "name",
            "description",
            "event_type",
            "start_date",
            "start_time",
            "end_date",
            "end_time",
            # "duration",
            "country",
            "goals",
            "target_age",
            "target_gender",
            "target_income",
            "communication_channel",
            "target_interests",
            "target_occupation"
        ]


class CampaignSerializer(serializers.ModelSerializer):
    business = serializers.StringRelatedField(read_only=True, source='business.id')

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
            "budget",
            "creative_asset",
            "breakdown",
            "target_age",
            "target_gender",
            "target_income_level",
            "occupation",
            "location",
            "interests",
            "communication_channel",
            "content_formats",
            "distribution_channels",
            "offer_description",
            "offer_terms"
        ]


class CampaignInfluencerSerializer(serializers.ModelSerializer):
    influencer = InfluencerSerializer(read_only=True)

    class Meta:
        model = CampaignInfluencers
        fields = ['id', 'influencer', 'business', 'confirmed', 'campaign']


class EventListOptSerializer(serializers.ModelSerializer):
    influencer = InfluencerSerializer(read_only=True)

    class Meta:
        model = EventInfluencer
        fields = ['id', 'event', 'influencer', 'confirmed']
