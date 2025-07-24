from django.contrib import admin
from .models import Submission, Leaderboard

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'challenge', 'score', 'status','code')

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'contest', 'total_score', 'total_time')
