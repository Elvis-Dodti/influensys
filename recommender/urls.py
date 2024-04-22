from django.urls import path

from recommender.views import *


urlpatterns = [
    path('get-recommendations/<int:marketer_id>/', fetch_data)
]