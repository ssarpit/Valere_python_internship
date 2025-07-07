from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from challenges.models import Challenge, TestCase
from submissions.models import Submission
import contextlib, io, threading, time
from django.db import models


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_code(request, challenge_id):
    try:
        user = request.user
        code = request.data.get("code", "").strip()

        if not code:
            return Response({"error": "Empty code!"}, status=400)

        challenge = Challenge.objects.get(id=challenge_id)

        Submission.objects.create(
            user=user,
            challenge=challenge,
            code=code,
            status='Accepted',  # Admin will decide later
            score=0
        )

        return Response({"message": "Submission stored successfully! Awaiting review."})

    except Challenge.DoesNotExist:
        return Response({"error": "Challenge not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['GET'])
def leaderboard(request):
    from django.db.models import Max

    # Get best score for each user per challenge
    from submissions.models import Submission

    leaderboard = (
        Submission.objects
        .filter(status='Accepted')
        .values('user__username')
        .annotate(total_score=models.Sum('score'))
        .order_by('-total_score')
    )

    return Response(list(leaderboard))
