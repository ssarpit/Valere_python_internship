from django.urls import path
# from .views import ChallengeListAPI, SubmitCodeAPI
from . import views
from api.views import execute_code
from .views import leaderboard
urlpatterns = [
    # path('challenges/', ChallengeListAPI.as_view(), name='api_challenge_list'),
    path('submit/<int:challenge_id>/', views.submit_code, name='submit_code'),
    path('execute/<int:challenge_id>/', execute_code, name='execute_code'),
    path('leaderboard/', leaderboard, name='leaderboard_api'),
]
