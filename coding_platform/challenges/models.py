from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField


class Challenge(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    time_limit = models.FloatField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='challenges_created'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TestCase(models.Model):
    challenge = models.ForeignKey(
        Challenge,
        on_delete=models.CASCADE,
        related_name='test_cases'
    )
    input = models.TextField()
    expected_output = models.TextField()
    is_hidden = models.BooleanField(default=True)

    def __str__(self):
        return f"TestCase (Hidden: {self.is_hidden}) for {self.challenge.title}"
