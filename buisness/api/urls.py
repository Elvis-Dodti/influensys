from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from buisness.api.views import *

urlpatterns = [
    path('buisness/create', BuisnessCreateAPIView.as_view(), name='buisness-create'),
    path('buisness/<int:pk>',BuisnessRUDView.as_view(), name='buisness-rud'),
    path('<str:slug>/events/create', EventCreateAPIView.as_view(), name='event-create'),
    path('<str:slug>/events/<int:pk>', EventRUDView.as_view(), name='event-rud'),
    path('<str:slug>/events/list', EventListAPIView.as_view(), name='event-list'),
    path('<str:slug>/campaigns/create', CampaignCreateAPIView.as_view(), name='campaign-create'),
]