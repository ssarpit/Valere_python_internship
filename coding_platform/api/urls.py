from django.urls import path
# from .views import ChallengeListAPI, SubmitCodeAPI
from . import views
from api.views import execute_code
from .views import leaderboard
urlpatterns = [
    path('contests/<int:contest_id>/challenges/', views.list_contest_challenges, name='list_contest_challenges'),
    path('submit/<int:challenge_id>/', views.submit_code, name='submit_code'),
    path('execute/<int:challenge_id>/', execute_code, name='execute_code'),
    path('leaderboard/', leaderboard, name='leaderboard_api'),
]
