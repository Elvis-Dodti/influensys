from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from buisness.api.views import *

urlpatterns = [
    path('buisness/create', BuisnessCreateAPIView.as_view(), name='buisness-create'),
    path('buisness/<int:pk>', BuisnessRUDView.as_view(), name='buisness-rud'),
    path('buisness/goals/create', BuisnessGoalsCreateAPIView.as_view(), name='buisness-goals-create'),
    path('buisness/goals/<int:pk>', BuisnessGoalsRUDView.as_view(), name='buisness-goals-rud'),
    path('<str:slug>/events/create', EventCreateAPIView.as_view(), name='event-create'),
    path('<str:slug>/events/<int:pk>', EventRUDView.as_view(), name='event-rud'),
    path('<str:slug>/events/list', EventListAPIView.as_view(), name='event-list'),
    path('<str:slug>/campaigns/create', CampaignCreateAPIView.as_view(), name='campaign-create'),
    path('<str:slug>/campaigns/<int:pk>', CampaignRUDView.as_view(), name='campaign-rud'),
    path('<str:slug>/campaigns/list', CampaignListAPIView.as_view(), name='campaign-list'),

]
