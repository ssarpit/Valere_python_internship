from django.contrib import admin
from .models import (
    Contest,
    ContestChallenge,
    ContestSubmission,
    ContestParticipation  # ✅ updated model name
)

@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'created_by')
    list_filter = ('start_time', 'end_time', 'created_by')
    search_fields = ('title', 'description')

@admin.register(ContestChallenge)
class ContestChallengeAdmin(admin.ModelAdmin):
    list_display = ('contest', 'challenge')
    list_filter = ('contest',)
    search_fields = ('contest__title', 'challenge__title')

@admin.register(ContestParticipation)  # ✅ updated here
class ContestParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'contest', 'start_time', 'submit_time', 'has_submitted')
    list_filter = ('has_submitted', 'contest')
    search_fields = ('user__username', 'contest__title')

@admin.register(ContestSubmission)
class ContestSubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'contest', 'submitted_at')
    list_filter = ('contest',)
    search_fields = ('user__username', 'contest__title')
