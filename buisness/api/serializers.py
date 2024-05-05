from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from sklearn.gaussian_process.kernels import Product

from buisness.models import *


class BuisnessSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    # image = Base64ImageField(required=False)

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
            "image",
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
            "slug",
            "image"
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
            "image",
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
            "remaining_budget",
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
            "offer_terms",
            "message",
            "image"
        ]


class CampaignInfluencerSerializer(serializers.ModelSerializer):
    influencer = InfluencerSerializer(read_only=True)

    class Meta:
        model = CampaignInfluencers
        fields = ['id', 'influencer', 'business', 'confirmed', 'campaign', 'status', 'cost', 'transaction_id']


class EventListOptSerializer(serializers.ModelSerializer):
    influencer = InfluencerSerializer(read_only=True)

    class Meta:
        model = EventInfluencer
        fields = ['id', 'event', 'influencer', 'confirmed', 'status']


class CampaignInfluencersSerailizer(serializers.ModelSerializer):
    influencer = InfluencerSerializer(read_only=True)
    business = BuisnessSerializer(read_only=True)

    class Meta:
        model = CampaignInfluencers
        fields = ['id', 'business', 'campaign', 'influencer', 'confirmed',
                  'status', 'cost', 'transaction_id']


class InfluencerWorkSerializer(serializers.ModelSerializer):
    campaign = CampaignSerializer(read_only=True)
    influencer = InfluencerSerializer(read_only=True)

    class Meta:
        model = InfluencerWork
        fields = ['id', 'campaign', 'influencer', 'video', 'marketer_response', 'confirmation', 'comments']


class ProductSerializer(serializers.ModelSerializer):
    business = BuisnessSerializer(read_only=True)

    class Meta:
        model = Products
        fields = ['id', 'name', 'image', 'specification', 'price', 'business']


class GiftSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    influencer = InfluencerSerializer(read_only=True)

    class Meta:
        model = Gifts
        fields = ['id', 'product', 'influencer', 'message', 'confirmation',
                  'amount']


class YoutubeInsightsSerializer(serializers.ModelSerializer):
    business = BuisnessSerializer(read_only=True)

    class Meta:
        model = YoutubeInsights
        fields = '__all__'


class InfluencerInsightsSerializer(serializers.ModelSerializer):
    influencer = InfluencerSerializer(read_only=True)

    class Meta:
        model = InfluencerInsights
        fields = '__all__'
