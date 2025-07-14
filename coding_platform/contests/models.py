from django.db import models
from challenges.models import Challenge
from django.db import models
from django.conf import settings
from django.db import models


# from .models import Contest


class Contest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contests_created')

    def __str__(self):
        return self.title


class ContestChallenge(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name='contest_challenges')
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='contest_challenges')
    
    class Meta:
        unique_together = ('contest', 'challenge')

    def __str__(self):
        return f"{self.challenge.title} in {self.contest.title}"



class ContestParticipation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    submit_time = models.DateTimeField(null=True, blank=True)
    has_submitted = models.BooleanField(default=False)
    total_score = models.IntegerField(default=0)

    time_taken_seconds = models.IntegerField(default=0)  # ✅ for sorting
    time_taken_display = models.CharField(max_length=20, blank=True, default="")  # ✅ for showing e.g. "10m:15s"

    class Meta:
        unique_together = ('user', 'contest')

    def __str__(self):
        return f"{self.user.username} - {self.contest.title} ({self.total_score} pts in {self.time_taken_display})"

class ContestSubmission(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    time_taken = models.PositiveIntegerField(default=0)
    class Meta:
        unique_together = ['contest', 'user']

    def __str__(self):
        return f"{self.user.username} submitted {self.contest.title}"
