from django.contrib import admin
from .models import Submission

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'challenge', 'status', 'submission_time')
    list_filter = ('status',)
    actions = ['accept_submission', 'reject_submission']

    @admin.action(description="✅ Mark as Accepted")
    def accept_submission(self, request, queryset):
        queryset.update(status='Accepted')

    @admin.action(description="❌ Mark as Rejected")
    def reject_submission(self, request, queryset):
        queryset.update(status='Rejected')
