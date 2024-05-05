from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView

from influensys.api.serializers import *


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
        business = Businesses.objects.get(slug=self.kwargs['slug'])
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


class EventRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Events.objects.filter(pk=self.kwargs['pk'])


class EventListAPIView(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Events.objects.filter(business__slug=self.kwargs['slug'])


class EventAllListAPIView(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Events.objects.all()


class CampaignStatusLists(ListAPIView):
    serializer_class = CampaignInfluencerSerializer

    def get_queryset(self):
        return CampaignInfluencers.objects.filter(business__slug=self.kwargs['slug'],
                                                  campaign__id=self.kwargs['pk'])


class CampaignCreateAPIView(CreateAPIView):
    serializer_class = CampaignSerializer

    def create(self, request, *args, **kwargs):
        business = Businesses.objects.get(slug=self.kwargs['slug'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(business=business)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampaignRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = CampaignSerializer

    def get_queryset(self):
        return Campaigns.objects.filter(id=self.kwargs['pk'])


class CampaignListAPIView(ListAPIView):
    serializer_class = CampaignSerializer

    def get_queryset(self):
        return Campaigns.objects.filter(business__slug=self.kwargs['slug'])


@api_view(['POST'])
def influencer_campaign_add(request, slug, id):
    business = Businesses.objects.get(slug=slug)
    campaign = Campaigns.objects.get(id=id)
    influencer = Influencers.objects.get(id=request.data['influencer'])

    if CampaignInfluencers.objects.filter(campaign=campaign, influencer=influencer, business=business).exists():
        context = {
            'message': 'Request already sent'
        }
        return Response(context, status=status.HTTP_200_OK)
    else:
        CampaignInfluencers.objects.create(campaign=campaign, influencer=influencer, business=business,
                                           cost=request.data['cost'])

    return Response(status=status.HTTP_201_CREATED)


class CampaignInfluencersRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = CampaignInfluencerSerializer

    def get_queryset(self):
        return CampaignInfluencers.objects.filter(id=self.kwargs['pk'])


class EventOptRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = EventOptInSerializer

    def get_queryset(self):
        return EventInfluencer.objects.filter(id=self.kwargs['pk'])


class EventOptList(ListAPIView):
    serializer_class = EventListOptSerializer

    def get_queryset(self):
        return EventInfluencer.objects.filter(event__id=self.kwargs['pk'])


class EventOptListConfirmed(ListAPIView):
    serializer_class = EventOptInSerializer

    def get_queryset(self):
        return EventInfluencer.objects.filter(business__slug=self.kwargs['slug'],
                                              event__id=self.kwargs['pk'],
                                              confirmed=True)


@api_view(['POST'])
def accept_influencer_event(request, slug, event_id, influencer_id):
    event_opt = EventInfluencer.objects.get(event__id=event_id, influencer__id=influencer_id)
    event_opt.confirmed = request.data.get('confirmed')
    if request.data.get('confirmed'):
        event_opt.status = 'Approved'
    else:
        event_opt.status = 'Rejected'

    event_opt.save()
    return Response(status=status.HTTP_200_OK)


class CampaignWorkRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = InfluencerWorkSerializer

    def get_queryset(self):
        return InfluencerWork.objects.filter(id=self.kwargs['pk'])


class CampaignWorkPerCampaignList(ListAPIView):
    serializer_class = InfluencerWorkSerializer

    def get_queryset(self):
        return InfluencerWork.objects.filter(campaign__id=self.kwargs['pk'])

class CampaignWorkPCIList(RetrieveAPIView):
    serializer_class = InfluencerWorkSerializer

    def get_queryset(self):
        return InfluencerWork.objects.filter(campaign__id=self.kwargs['pk'],
                                             influencer__id=self.kwargs['influencer_id']).order_by('-id')[:1]


@api_view(['POST'])
def accept_influencer_work(request, influencer_work_id):
    work = InfluencerWork.objects.get(id=influencer_work_id)
    transaction = CampaignInfluencers.objects.get(influencer__id=work.influencer.id,
                                                  campaign__id=work.campaign.id)
    if request.data.get('confirmed'):
        work.confirmation = 'Approved'
        transaction.transaction_id = request.data.get('transaction_id')
    else:
        work.confirmation = 'Rejected'
        work.comments = ''
        work.video = ''
        work.save()

    return Response(status=status.HTTP_200_OK)


class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        business = Businesses.objects.get(slug=self.kwargs['slug'])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(business=business)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Products.objects.filter(id=self.kwargs['pk'])


class ProductsList(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Products.objects.filter(business__slug=self.kwargs['slug'])


class GiftsCreateView(CreateAPIView):
    serializer_class = GiftSerializer

    def create(self, request, *args, **kwargs):
        products = Products.objects.filter(id__in=request.data.pop('products'))
        business = Businesses.objects.get(slug=self.kwargs['slug'])
        influencer = Influencers.objects.get(id=request.data.pop('influencer_id'))
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(business=business, influencer=influencer)
            gift = Gifts.objects.get(id=serializer.data['id'])
            gift.product.add(*products)
            gift.save()

            return Response(self.get_serializer(gift).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GiftsListView(ListAPIView):
    serializer_class = GiftSerializer

    def get_queryset(self):
        return Gifts.objects.filter(business__slug=self.kwargs['slug'])


@api_view(['POST'])
def influencer_filter(request, *args, **kwargs):
    influencers = Influencers.objects.filter(industry__contains=request.data.get('query'))
    return Response(InfluencerSerializer(influencers).data, status=status)


class YouTubeCreateView(CreateAPIView):
    serializer_class = YoutubeInsightsSerializer

    def create(self, request, *args, **kwargs):
        business = Businesses.objects.get(id=request.data.pop('business'))
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(business=business)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class YoutubeRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = YoutubeInsightsSerializer

    def get_queryset(self):
        return YoutubeInsights.objects.filter(buisness__id=self.kwargs['business_id'])


class YoutubeInfluencerRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = InfluencerInsightsSerializer

    def get_queryset(self):
        return InfluencerInsights.objects.filter(influencer__id=self.kwargs['pk'])
