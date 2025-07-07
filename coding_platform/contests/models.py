from django.db import models
from django.conf import settings
from challenges.models import Challenge

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
    # challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='contest_challenges')
    # challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='contest_challenges')
    
    class Meta:
        unique_together = ('contest', 'challenge')

    def __str__(self):
        return f"{self.challenge.title} in {self.contest.title}"


class UserContest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    submitted = models.BooleanField(default=False)


class ContestSubmission(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    time_taken = models.IntegerField(null=True, blank=True)
    class Meta:
        unique_together = ['contest', 'user']

    def __str__(self):
        return f"{self.user.username} submitted {self.contest.title}"
