from django.urls import path
from . import views


app_name = 'contests'  # ← ADD THIS

urlpatterns = [
    path('<int:contest_id>/leaderboard/', views.contest_leaderboard, name='contest_leaderboard'),
    path('<int:contest_id>/join/',views. join_contest, name='join_contest'),
    path('<int:contest_id>/', views.contest_detail, name='contest_detail'),
]
