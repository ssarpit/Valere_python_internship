from django.shortcuts import render, get_object_or_404,redirect
from .models import Contest, ContestParticipant
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


@login_required
def contest_leaderboard(request, contest_id):
    contest = get_object_or_404(Contest, id=contest_id)
    leaderboard = Leaderboard.objects.filter(contest=contest).order_by('-total_score', 'total_time')
    return render(request, 'contests/leaderboard.html', {
        'contest': contest,
        'leaderboard': leaderboard
    })


@login_required
def contest_detail(request, contest_id):
    contest = get_object_or_404(Contest, pk=contest_id)
    all_challenges = Challenge.objects.filter(contest_challenges__contest=contest)

    # ✅ Get solved challenge IDs
    solved_challenges = Submission.objects.filter(
        user=request.user,
        challenge__in=all_challenges,
        status="Accepted"
    ).values_list('challenge_id', flat=True)

    total = all_challenges.count()
    solved = len(set(solved_challenges))

    return render(request, 'contests/contest_detail.html', {
        'contest': contest,
        'challenges': all_challenges,
        'solved_challenges': solved_challenges,
        'all_solved': total == solved,
    })

@login_required
# Optional view if needed for "Join" action
def join_contest(request, contest_id):
    contest = get_object_or_404(Contest, pk=contest_id)
    return redirect('contests:contest_detail', contest_id=contest.id)
