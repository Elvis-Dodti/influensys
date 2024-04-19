from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from influensys.api.views import *

urlpatterns = [
    path('influencer/create', InfluencerCreateView.as_view(), name='influencer-create'),
    path('influencer/<int:pk>', InfluencerRUDView.as_view(), name='influencer-rud'),
    path('influencer/list', InfluencerListView.as_view(), name='influencer-list'),
    path('<str:slug>/target-info/add', InfluencerTargetCreate.as_view(), name='influencer-target'),
    path('<str:slug>/target-info/<int:pk>', InfluencerTargetRUD.as_view(), name='influencer-target-rud'),

    # insta
    path('influencer/insta/', instagram_token_add),

    # opt event
    path('<str:slug>/event/opt-in', opt_event, name='opt-in'),
    path('<str:slug>/events/opt-in/list', EventOptListInfluencer.as_view(), name='opt-in-list'),

    # campaign
    path('<str:slug>/campaign/status-info/list/', CampaignStatusListsInfluencer.as_view(), name='campaign-status'),
    path('<str:slug>/campaign-confirm/<int:campaign_id>/', accept_campaign),

]
