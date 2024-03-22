from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import *
from rest_framework.response import Response

from buisness.models import *
from buisness.api.serializers import *


class BuisnessCreateAPIView(CreateAPIView):
    serializer_class = BuisnessSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BuisnessRUDView(RetrieveUpdateAPIView):
    serializer_class = BuisnessSerializer

    def get_queryset(self):
        return Businesses.objects.filter(pk=self.kwargs['pk'])


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
