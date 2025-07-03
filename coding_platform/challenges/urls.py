from django.urls import path
from . import views

app_name = 'challenges'

urlpatterns = [
    path('<int:challenge_id>/', views.challenge_detail, name='challenge_detail'),
    # path('', views.challenge_list, name='challenge_list'),
    # path('challenge_detail/', views.challenge_detail, name='challenge_detail'),
    path('<int:challenge_id>/submit/', views.submit_code, name='submit_code'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),  # ✅ Add this
]
