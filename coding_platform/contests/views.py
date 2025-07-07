from django.shortcuts import render, get_object_or_404,redirect
from .models import Contest
from submissions.models import Leaderboard
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from challenges.models import Challenge
from django.shortcuts import redirect, get_object_or_404
from .models import Contest
from django.shortcuts import render, get_object_or_404
from .models import Contest, ContestChallenge
from challenges.models import Challenge
from submissions.models import Submission
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contest, ContestSubmission
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Contest, UserContest, ContestChallenge
from django.utils.timezone import now as tz_now
from contests.models import UserContest

from contests.models import ContestSubmission
from submissions.models import Submission
from django.contrib.auth.models import User
from django.db.models import Count, Min
@login_required
def leaderboard(request):
    contest_submissions = ContestSubmission.objects.select_related('user', 'contest')
    leaderboard = []

    for entry in contest_submissions:
        user = entry.user
        solved = Submission.objects.filter(
            user=user,
            status='Accepted'
        ).values('challenge').distinct()
        leaderboard.append({
            'user': user,
            'total_score': solved.count(),
            'total_time': (entry.submitted_at - user.date_joined).total_seconds()
        })

    leaderboard.sort(key=lambda x: (-x['total_score'], x['total_time']))

    return render(request, 'challenges/leaderboard.html', {
        'leaderboard': leaderboard
    })


@login_required
def contest_detail(request, contest_id):
    contest = get_object_or_404(Contest, pk=contest_id)

    # Always create or get user's contest session
    user_contest, created = UserContest.objects.get_or_create(
        user=request.user,
        contest=contest
    )
    started_at = user_contest.started_at

    # Get all challenges in the contest
    contest_challenges = ContestChallenge.objects.filter(contest=contest).select_related('challenge')
    challenges = [cc.challenge for cc in contest_challenges]
    challenge_ids = [c.id for c in challenges]

    # Get solved and attempted challenge IDs
    solved_qs = Submission.objects.filter(
        user=request.user,
        challenge_id__in=challenge_ids,
        status='Accepted'
    ).values_list('challenge_id', flat=True).distinct()
    solved_challenges = set(solved_qs)

    attempted_qs = Submission.objects.filter(
        user=request.user,
        challenge_id__in=challenge_ids
    ).values_list('challenge_id', flat=True).distinct()

    all_attempted = set(challenge_ids) == set(attempted_qs)
    all_solved = set(challenge_ids) == solved_challenges

    already_submitted = ContestSubmission.objects.filter(
        user=request.user, contest=contest
    ).exists()

    return render(request, 'contests/contest_detail.html', {
        'contest': contest,
        'challenges': challenges,
        'solved_challenges': solved_challenges,
        'all_attempted': all_attempted,
        'all_solved': all_solved,
        'already_submitted': already_submitted,
        'started_at': started_at,
    })




from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Contest, ContestSubmission

import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ContestSubmission  # or wherever your model is
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# views.py

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from .models import Contest, UserContest



def submit_contest(request, contest_id):
    if request.method == "POST":
        data = json.loads(request.body)
        time_taken = data.get('time_taken')

        contest = get_object_or_404(Contest, id=contest_id)
        submission, created = ContestSubmission.objects.get_or_create(
            user=request.user,
            contest=contest
        )

        submission.time_taken = time_taken
        submission.save()

        return JsonResponse({"message": "Contest submitted successfully!"})

@login_required
# Optional view if needed for "Join" action
def join_contest(request, contest_id):
    contest = get_object_or_404(Contest, pk=contest_id)
    return redirect('contests:contest_detail', contest_id=contest.id)

from .models import ContestSubmission
# views.py

def leaderboard(request):
    leaderboard = UserContest.objects.select_related('user').order_by('-total_score', 'time_taken')
    return render(request, 'challenges/leaderboard.html', {'leaderboard': leaderboard})
