from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from submissions.models import Submission
from django.db import models 
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from submissions.models import Submission
from rest_framework.response import Response
from .models import Contest, ContestChallenge,  ContestSubmission
from submissions.models import Submission
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.utils.timezone import now
from contests.models import ContestParticipation



@permission_classes([IsAuthenticated])
@login_required
def contest_detail(request, contest_id):
    contest = get_object_or_404(Contest, pk=contest_id)

    # Ensure participation entry exists
    user_contest, _ = ContestParticipation.objects.get_or_create(user=request.user, contest=contest)
    start_time = user_contest.start_time

    # Get all challenges linked to this contest
    contest_challenges = ContestChallenge.objects.filter(contest=contest).select_related('challenge')
    challenges = [cc.challenge for cc in contest_challenges]

    # Check if user has already submitted the contest
    already_submitted = ContestSubmission.objects.filter(
        user=request.user,
        contest=contest
    ).exists()

    return render(request, 'contests/contest_detail.html', {
        'contest': contest,
        'challenges': challenges,
        'already_submitted': already_submitted,
        'started_at': start_time,
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def start_contest(request, contest_id):
    contest = Contest.objects.get(id=contest_id)
    participation, created = ContestParticipation.objects.get_or_create(
        user=request.user, contest=contest
    )
    if not created:
        return Response({"message": "Already started"}, status=400)
    return Response({"message": "Contest started", "start_time": participation.start_time})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_contest(request, contest_id):
    try:
        participation = ContestParticipation.objects.get(user=request.user, contest_id=contest_id)
        if participation.has_submitted:
            return Response({"message": "Already submitted!"}, status=400)

        # ✅ Safely extract data from DRF's request.data
        time_taken_seconds = request.data.get("time_taken_seconds")
        time_taken_display = request.data.get("time_taken_display")

        participation.submit_time = now()
        participation.has_submitted = True
        participation.time_taken_seconds = time_taken_seconds or 0
        participation.time_taken_display = time_taken_display or "N/A"
        participation.save()

        return Response({"message": "Contest submitted!"})
    except ContestParticipation.DoesNotExist:
        return Response({"error": "Participation not found"}, status=404)



