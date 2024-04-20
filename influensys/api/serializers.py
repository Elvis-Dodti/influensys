from buisness.api.serializers import *





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
