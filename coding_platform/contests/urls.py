from django.urls import path
from . import views
from .views import submit_contest


app_name = 'contests'  # ← ADD THIS

urlpatterns = [
    path('<int:contest_id>/leaderboard/', views.leaderboard, name='leaderboard'),
    path('<int:contest_id>/join/',views. join_contest, name='join_contest'),
    path('<int:contest_id>/', views.contest_detail, name='contest_detail'),
    path('submit_contest/<int:contest_id>/', submit_contest, name='submit_contest'),
    
]

