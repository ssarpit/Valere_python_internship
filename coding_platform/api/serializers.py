# api/serializers.py
from rest_framework import serializers
from challenges.models import Challenge

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id', 'title', 'description']  

