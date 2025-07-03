from django.urls import path
from .views import ChallengeListAPI, SubmitCodeAPI

urlpatterns = [
    path('challenges/', ChallengeListAPI.as_view(), name='api_challenge_list'),
    path('submit/', SubmitCodeAPI.as_view(), name='api_submit_code'),
]
