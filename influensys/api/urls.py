from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from influensys.api.views import *

urlpatterns = [
    path('influencer/create', InfluencerCreateView.as_view(), name='influencer-create'),
    path('influencer/<int:pk>', InfluencerRUDView.as_view(), name='influencer-rud'),
    path('influencer/list', InfluencerListView.as_view(), name='influencer-list'),

    # insta
    path('influencer/insta/', instagram_token_add),

]