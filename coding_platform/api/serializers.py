from rest_framework import serializers
from challenges.models import Challenge, TestCase
from submissions.models import Submission
from django.contrib.auth.models import User

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id', 'title', 'description', 'time_limit']

# serializers.py
class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'challenge', 'code', 'user', 'status', 'execution_time', 'score', 'submitted_at']
        read_only_fields = ['user', 'status', 'execution_time', 'score', 'submitted_at']


    def create(self, validated_data):
        validated_data['submitted_by'] = self.context['request'].user
        return super().create(validated_data)