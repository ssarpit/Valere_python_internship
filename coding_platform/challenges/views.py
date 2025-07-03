from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
import io, contextlib

from .models import Challenge, TestCase
from submissions.models import Submission
from contests.models import ContestChallenge


@login_required
def challenge_detail(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    sample_testcases = challenge.test_cases.filter(is_hidden=False)

    return render(request, 'challenges/challenge_detail.html', {
        'challenge': challenge,
        'sample_testcases': sample_testcases,
    })


@login_required
def submit_code(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    user = request.user

    if request.method == 'POST':
        code = request.POST['code']
        test_cases = challenge.test_cases.filter(is_hidden=True)

        result = "Accepted"
        for test in test_cases:
            try:
                lines = test.input.strip().split('\n')
                idx = 0
                def fake_input():
                    nonlocal idx
                    val = lines[idx]
                    idx += 1
                    return val

                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    exec(code, {'input': fake_input})

                if output.getvalue().strip() != test.expected_output.strip():
                    result = "Wrong Answer"
                    break
            except Exception:
                result = "Runtime Error"
                break

        Submission.objects.create(
            user=user,
            challenge=challenge,
            code=code,
            status=result,
        )

        # ✅ Redirect to contest detail if challenge is part of a contest
        contest_challenge = challenge.contest_challenges.first()
        if contest_challenge:
            return redirect('contests:contest_detail', contest_id=contest_challenge.contest.id)
        else:
            return redirect('dashboard')  # fallback

    return redirect('challenges:challenge_detail', challenge_id=challenge.id)  # fallback for GET


@login_required
def leaderboard_view(request):
    leaderboard = Submission.objects.values('user__username') \
        .annotate(total_submissions=Count('id')) \
        .order_by('-total_submissions')

    return render(request, 'challenges/leaderboard.html', {'leaderboard': leaderboard})
