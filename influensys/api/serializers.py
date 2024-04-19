from rest_framework import serializers
from influensys.models import *


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
