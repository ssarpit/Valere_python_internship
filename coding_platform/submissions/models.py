from django.db import models
from django.conf import settings
from challenges.models import Challenge
from contests.models import Contest

from django.db import models
from django.conf import settings
from challenges.models import Challenge

class Submission(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    code = models.TextField()
    score = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    submission_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.challenge.title} ({self.status})'


class Leaderboard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='leaderboard_entries')
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name='leaderboard_entries')
    total_score = models.IntegerField()
    total_time = models.FloatField()

    class Meta:
        unique_together = ('user', 'contest')

    def __str__(self):
        return f"{self.user.username} - {self.contest.title}"
