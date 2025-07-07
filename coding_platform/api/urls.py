from django.urls import path
# from .views import ChallengeListAPI, SubmitCodeAPI
from . import views
from .views import leaderboard
urlpatterns = [
    # path('challenges/', ChallengeListAPI.as_view(), name='api_challenge_list'),
    # path('submit/', SubmitCodeAPI.as_view(), name='api_submit_code'),
    path('submit/<int:challenge_id>/', views.submit_code, name='submit_code'),
    path('leaderboard/', leaderboard, name='leaderboard_api'),
]
