from django.urls import path
from . import views
from .views import submit_contest
from django.urls import path


app_name = 'contests'  # ← ADD THIS

urlpatterns = [
    # path('<int:contest_id>/leaderboard/', views.leaderboard, name='leaderboard'),
    path('<int:contest_id>/', views.contest_detail, name='contest_detail'),
    path('submit_contest/<int:contest_id>/', submit_contest, name='submit_contest'),
    # path('<int:contest_id>/live_leaderboard/', views.live_leaderboard, name='live_leaderboard'),
    
]

