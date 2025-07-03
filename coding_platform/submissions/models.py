from django.db import models
from django.conf import settings
from challenges.models import Challenge
from contests.models import Contest

class Submission(models.Model):
    STATUS_CHOICES = [
        ('Accepted', 'Accepted'),
        ('Wrong Answer', 'Wrong Answer'),
        ('Time Limit Exceeded', 'Time Limit Exceeded'),
        ('Compilation Error', 'Compilation Error'),
        ('Runtime Error', 'Runtime Error'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='submissions')
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='submissions')
    contest = models.ForeignKey(Contest, on_delete=models.SET_NULL, null=True, blank=True, related_name='submissions')
    code = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    execution_time = models.FloatField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.user.username}'s submission to {self.challenge.title}"


class Leaderboard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='leaderboard_entries')
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name='leaderboard_entries')
    total_score = models.IntegerField()
    total_time = models.FloatField()

    class Meta:
        unique_together = ('user', 'contest')

    def __str__(self):
        return f"{self.user.username} - {self.contest.title}"
