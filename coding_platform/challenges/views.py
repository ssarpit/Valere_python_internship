from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
import io, contextlib
from .models import Challenge
from submissions.models import Submission
from contests.models import ContestChallenge
from django.utils.timezone import now
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
import subprocess
import tempfile
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Challenge, TestCase
from submissions.models import Submission


@permission_classes([IsAuthenticated])
@login_required

@login_required
def challenge_detail(request, challenge_id):
    challenge = get_object_or_404(Challenge, id=challenge_id)
    sample_testcases = TestCase.objects.filter(challenge=challenge, is_hidden=False)

    # ✅ Get the user's last submission
    previous_submission = Submission.objects.filter(
        user=request.user,
        challenge=challenge
    ).order_by('-id').first()

    return render(request, 'challenges/challenge_detail.html', {
        'challenge': challenge,
        'sample_testcases': sample_testcases,
        'previous_submission': previous_submission
    })

@login_required
def leaderboard_view(request):
    leaderboard = Submission.objects.values('user__username') \
        .annotate(total_submissions=Count('id')) \
        .order_by('-total_submissions')

    return render(request, 'challenges/leaderboard.html', {'leaderboard': leaderboard})



# @csrf_exemp
