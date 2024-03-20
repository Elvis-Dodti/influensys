from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import *
from rest_framework.response import Response

from influensys.api.serializers import *
from influensys.models import *


class InfluencerCreateView(CreateAPIView):
    serializer_class = InfluencerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InfluencerRUDView(RetrieveUpdateAPIView):
    serializer_class = InfluencerSerializer

    def get_queryset(self):
        return Influencers.objects.filter(pk=self.kwargs['pk'])