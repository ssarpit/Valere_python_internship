from rest_framework import generics
from challenges.models import Challenge
from submissions.models import Submission
from .serializers import ChallengeSerializer, SubmissionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ChallengeListAPI(generics.ListAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

class SubmitCodeAPI(generics.CreateAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]


    