from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from buisness.api.views import *

urlpatterns = [
    path('buisness/create', BuisnessCreateAPIView.as_view(), name='buisness-create'),
    path('buisness/<int:pk>', BuisnessRUDView.as_view(), name='buisness-rud'),
    path('<str:slug>/goals/create', BuisnessGoalsCreateAPIView.as_view(), name='buisness-goals-create'),
    path('<str:slug>/goals/<int:pk>', BuisnessGoalsRUDView.as_view(), name='buisness-goals-rud'),
    path('<str:slug>/events/create', EventCreateAPIView.as_view(), name='event-create'),
    path('<str:slug>/events/<int:pk>', EventRUDView.as_view(), name='event-rud'),
    path('<str:slug>/events/list', EventListAPIView.as_view(), name='event-list'),
    path('events/list/all', EventAllListAPIView.as_view(), name='event-all-list'),
    path('<str:slug>/events/<int:pk>/status-info/list/', EventOptList.as_view(), name='event-all-list'),
    path('<str:slug>/events/<int:pk>/status-info/confirmed/list/', EventOptListConfirmed.as_view(), name='event-confirmed'),
    path('<str:slug>/events/status-info/<int:pk>/', EventOptRUD.as_view(), name='event-opt-rud'),
    path('<str:slug>/events/status-info/<int:event_id>/<int:influencer_id>/', accept_influencer_event, name='event-accept-influencer'),
    path('<str:slug>/campaign/status-info-business/<int:pk>/list/', CampaignStatusLists.as_view(), name='campaign-opt-status'),
    path('<str:slug>/campaigns/create', CampaignCreateAPIView.as_view(), name='campaign-create'),
    path('<str:slug>/campaigns/<int:pk>', CampaignRUDView.as_view(), name='campaign-rud'),
    path('<str:slug>/campaigns/list', CampaignListAPIView.as_view(), name='campaign-list'),
    path('<str:slug>/campaigns/<int:id>/add-influencer', influencer_campaign_add, name='influencer-campaign-add'),

]
