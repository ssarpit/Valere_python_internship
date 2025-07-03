from rest_framework import serializers
from challenges.models import Challenge, TestCase
from submissions.models import Submission
from django.contrib.auth.models import User

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id', 'title', 'description', 'time_limit']

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'challenge', 'user', 'code', 'status', 'execution_time', 'submitted_at']

