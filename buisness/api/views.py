from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.response import Response

from influensys.api.serializers import InfluencerSerializer
from influensys.models import *
from buisness.models import *
from buisness.api.serializers import *


@api_view(['GET'])
def user_is(request):
    usr = User.objects.get(username=request.user)
    print(usr.id)
    if Businesses.objects.filter(user=usr).exists():
        context = {
            'is_business': True,
            'is_influencer': False,
            'business': BuisnessSerializer(Businesses.objects.filter(user=usr), many=True).data
        }

    elif Influencers.objects.filter(user=usr).exists():
        context = {
            'is_influencer': True,
            'is_business': False,
            'influencer': InfluencerSerializer(Influencers.objects.filter(user=usr), many=True).data
        }

    else:
        context = {
            'is_business': False,
            'is_influencer': False
        }
    return Response(context, status=status.HTTP_200_OK)


class BuisnessCreateAPIView(CreateAPIView):
    serializer_class = BuisnessSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BuisnessRUDView(RetrieveUpdateAPIView):
    serializer_class = BuisnessSerializer

    def get_queryset(self):
        return Businesses.objects.filter(pk=self.kwargs['pk'])


class BuisnessGoalsCreateAPIView(CreateAPIView):
    serializer_class = BusinessGoalsSerializer

    def create(self, request, *args, **kwargs):
        business = Businesses.objects.get(pk=self.kwargs['slug'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(business=business)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BuisnessGoalsRUDView(RetrieveUpdateAPIView):
    serializer_class = BusinessGoalsSerializer

    def get_queryset(self):
        return BusinessGoals.objects.filter(pk=self.kwargs['pk'])


class EventCreateAPIView(CreateAPIView):
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        business = Businesses.objects.get(slug=self.kwargs['slug'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(business=business)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventRUDView(RetrieveUpdateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Events.objects.filter(pk=self.kwargs['pk'])


class EventListAPIView(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Events.objects.filter(business__slug=self.kwargs['slug'])


class CampaignCreateAPIView(CreateAPIView):
    serializer_class = CampaignSerializer

    def create(self, request, *args, **kwargs):
        buisness = Businesses.objects.get(slug=self.kwargs['slug'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(business=buisness)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampaignRUDView(RetrieveUpdateAPIView):
    serializer_class = CampaignSerializer

    def get_queryset(self):
        return Campaigns.objects.filter(id=self.kwargs['pk'])


class CampaignListAPIView(ListAPIView):
    serializer_class = CampaignSerializer

    def get_queryset(self):
        return Campaigns.objects.filter(business__slug=self.kwargs['slug'])
