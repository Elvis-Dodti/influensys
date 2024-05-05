from django.shortcuts import render, redirect
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.response import Response

from buisness.api.serializers import *
from influensys.api.serializers import *
from influensys.models import *
from buisness.models import *
import os
from dotenv import load_dotenv

load_dotenv()


class InfluencerCreateView(CreateAPIView):
    serializer_class = InfluencerSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InfluencerRUDView(RetrieveUpdateAPIView):
    serializer_class = InfluencerSerializer

    def get_queryset(self):
        return Influencers.objects.filter(pk=self.kwargs['pk'])


class InfluencerListView(ListAPIView):
    serializer_class = InfluencerSerializer

    def get_queryset(self):
        return Influencers.objects.all()


class InfluencerTargetCreate(CreateAPIView):
    serializer_class = TargetInfoSerializer

    def create(self, request, *args, **kwargs):
        influencer = Influencers.objects.get(slug=self.kwargs['slug'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(influencer=influencer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InfluencerTargetRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = TargetInfoSerializer

    def get_queryset(self):
        return TargetInfo.objects.filter(id=self.kwargs['pk'])


@api_view(['GET'])
def instagram_redirect(request):
    return redirect(
        "https://api.instagram.com/oauth/authorize/?client_id={}&redirect_uri=https://influverse.vercel.app/&response_type=code"
        .format(os.environ.get('INSTAGRAM_CLIENT_ID')))


@api_view(['GET'])
def instagram_token_add(request):
    influencer = Influencers.objects.get(slug=request.GET.get('slug'))
    token = request.GET.get('code')
    InfluencerInstagramTokens.objects.create(influencer=influencer,
                                             token=token)
    return redirect('http://localhost:3000/influencer/completeprofile/')


@api_view(['POST'])
def opt_event(request, slug):
    infuencer = Influencers.objects.get(slug=slug)
    event = Events.objects.get(id=request.data.get('event'))
    if EventInfluencer.objects.filter(event=event, influencer=infuencer).exists():
        context = {
            'message': 'Request already sent'
        }
        return Response(context, status=status.HTTP_200_OK)
    else:
        EventInfluencer.objects.create(event=event, influencer=infuencer)

    return Response(status=status.HTTP_200_OK)


class CampaignStatusListsInfluencer(ListAPIView):
    serializer_class = CampaignOptSerializer

    def get_queryset(self):
        return CampaignInfluencers.objects.filter(influencer__slug=self.kwargs['slug'])


class EventOptListInfluencer(ListAPIView):
    serializer_class = EventOptInSerializer

    def get_queryset(self):
        return EventInfluencer.objects.filter(influencer__slug=self.kwargs['slug'])


@api_view(['POST'])
def accept_campaign(request, slug, campaign_id):
    campaign_opt = CampaignInfluencers.objects.get(campaign__id=campaign_id, influencer__slug=slug)
    campaign_opt.confirmed = request.data.get('confirmed')
    if request.data.get('confirmed'):
        campaign_opt.status = 'Approved'
        campaign = Campaigns.objects.get(id=campaign_id)
        campaign.remaining_budget = str(float(campaign.remaining_budget) - float(campaign_opt.cost))
    else:
        campaign_opt.status = 'Rejected'

    campaign_opt.save()
    return Response(status=status.HTTP_200_OK)


class CampaignOptRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = CampaignInfluencerSerializer

    def get_queryset(self):
        return CampaignInfluencers.objects.filter(id=self.kwargs['pk'])


class CampaignOptListConfirmed(ListAPIView):
    serializer_class = CampaignOptSerializer

    def get_queryset(self):
        return CampaignInfluencers.objects.filter(influencer__slug=self.kwargs['slug'],
                                                  status='Approved')


class CampaignWorkCreate(CreateAPIView):
    serializer_class = InfluencerWorkSerializer

    def create(self, request, *args, **kwargs):
        campaign = Campaigns.objects.get(id=self.kwargs.get('pk'))
        influencer = Influencers.objects.get(slug=self.kwargs['slug'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(campaign=campaign,
                            influencer=influencer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampaignWorkRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = InfluencerWorkSerializer

    def get_queryset(self):
        return InfluencerWork.objects.get(id=self.kwargs['pk'])

class CampaignWorkPCInfluencerList(ListAPIView):
    serializer_class = InfluencerWorkSerializer

    def get_queryset(self):
        val = InfluencerWork.objects.filter(campaign__id=self.kwargs['pk'],
                                             influencer__id=self.kwargs['influencer_id']).order_by('-id')
        return val[:1]

class InfluencerGifts(ListAPIView):
    serializer_class = GiftSerializer

    def get_queryset(self):
        return Gifts.objects.filter(influencer__slug=self.kwargs['slug'])


@api_view(['POST'])
def confirm_gift(request, slug, gift_id):
    gift = Gifts.objects.get(id=gift_id)
    print(gift)
    if request.data.get('confirmed'):
        gift.confirmation = 'Confirmed'
        gift.save()
    else:
        gift.confirmation = 'Rejected'
        gift.save()

    return Response(status=status.HTTP_200_OK)


class CampaignWorkListView(ListAPIView):
    serializer_class = InfluencerWorkSerializer

    def get_queryset(self):
        return InfluencerWork.objects.filter(influencer__slug=self.kwargs['slug'])


class InfluInsightCreateView(CreateAPIView):
    serializer_class = InfluencerInsightsSerializer

    def create(self, request, *args, **kwargs):
        influencer = Influencers.objects.get(id=request.data.pop('influencer'))
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(influencer=influencer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InfluInsightRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = InfluencerInsightsSerializer

    def get_queryset(self):
        return InfluencerInsights.objects.filter(influencer__id=self.kwargs['influencer_id'])
