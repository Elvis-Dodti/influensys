from rest_framework import serializers
from recommender.models import InfluensysInfluencers


class InfluencerSerializer(serializers.ModelSerializer):
    slug = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = InfluensysInfluencers
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


def serialize_recomendations(data):
    return {
        "id": data.id,
        "name": data.name,
        "description": data.description,
        "email": data.email,
        "phone": data.phone,
        "industry": data.industry,
        "address": data.address,
        "country": data.country,
        "pincode": data.pincode,
        "annual_revenue": data.annual_revenue,
        "facebook": data.facebook,
        "instagram": data.instagram,
        "website": data.website,
        "slug": data.slug
    }


class InfluencerQuickSerializer(serializers.Serializer):

    def to_representation(self, instance):
        return serialize_recomendations(instance)
