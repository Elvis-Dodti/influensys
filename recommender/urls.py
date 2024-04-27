from django.urls import path

from recommender.views import *


urlpatterns = [
    path('get-recommendations/<int:marketer_id>/', fetch_data_marketers),
    path('get-recommendations/top-influencers-match/<int:marketer_id>/', fetch_data_top_marketers),
    path('get-recommendations/campaign/<int:campaign_id>/', fetch_data_for_campaigns)

]