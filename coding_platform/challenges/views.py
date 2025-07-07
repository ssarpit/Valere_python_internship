from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
import io, contextlib

from .models import Challenge
from submissions.models import Submission
from contests.models import ContestChallenge
from django.utils.timezone import now


@login_required

def challenge_detail(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)    
    # ✅ Get the user's latest submission for this challenge, if any
    previous_submission = None
    if request.user.is_authenticated:
        previous_submission = Submission.objects.filter(
            user=request.user,
            challenge=challenge
            ).order_by('-submission_time').first()

    return render(request, 'challenges/challenge_detail.html', {
        'challenge': challenge,
        'previous_submission': previous_submission,
    })



@login_required

def submit_code(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)

    if request.method == 'POST':
        code = request.POST.get('code')

        # 🚨 Replace this with actual logic to check output vs test cases
        passed_all = True  # You can replace this later with logic

        Submission.objects.create(
            user=request.user,
            challenge=challenge,
            code=code,
            status='Accepted' if passed_all else 'Rejected',
            submission_time=now()
        )

        return redirect('challenges:challenge_detail', challenge_id=challenge.id)


@login_required
def leaderboard_view(request):
    leaderboard = Submission.objects.values('user__username') \
        .annotate(total_submissions=Count('id')) \
        .order_by('-total_submissions')

    return render(request, 'challenges/leaderboard.html', {'leaderboard': leaderboard})
