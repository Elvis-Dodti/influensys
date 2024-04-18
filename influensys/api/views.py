from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.response import Response

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
    EventInfluencer.objects.create(event=event, influencer=infuencer)
    return Response(status=status.HTTP_200_OK)