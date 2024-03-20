from rest_framework import serializers
from influensys.models import *


class InfluencerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Influencers
        fields = '__all__'
