from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from challenges.models import Challenge, TestCase
from submissions.models import Submission
from .utils import run_user_code
import traceback
from contests.models import ContestParticipation, ContestChallenge, Contest
from rest_framework.response import Response
from django.db.models import Sum
from django.core.cache import cache
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.cache import cache
from .serializers import ChallengeSerializer

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
            status='Accepted',
            score=0
        )

        # Invalidate relevant caches
        cache.delete("leaderboard_cache")
        if hasattr(challenge, 'contest'):
            cache.delete(f"contest_challenges_{challenge.contest.id}")

        return Response({"message": "Submission stored successfully! Awaiting review."})

    except Challenge.DoesNotExist:
        return Response({"error": "Challenge not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def leaderboard(request):
    cache_key = "leaderboard_cache"
    data = cache.get(cache_key)
    if not data:
        leaderboard = (
            ContestParticipation.objects
            .filter(has_submitted=True)
            .select_related('user', 'contest')
            .order_by('-total_score', 'time_taken_seconds')
            .values('user__username', 'total_score', 'time_taken_display')
        )
        data = list(leaderboard)
        cache.set(cache_key, data, timeout=60 * 3)  # Cache for 3 minutes

    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def execute_code(request, challenge_id):
    try:
        code = request.data.get("code", "")
        run_type = request.GET.get("type", "test")
        user = request.user

        challenge = Challenge.objects.get(id=challenge_id)
        contest = challenge.contest  # Ensure Challenge has FK to Contest

        # Check if user has already submitted the contest
        participation = ContestParticipation.objects.filter(user=user, contest=contest).first()
        if participation and participation.has_submitted and run_type == "final":
            return JsonResponse({"error": "Contest already submitted. No further submissions allowed."}, status=403)

        test_cases = TestCase.objects.filter(challenge=challenge)
        if run_type == "test":
            test_cases = test_cases.filter(is_hidden=False)

        formatted_cases = [{"input": t.input, "expected_output": t.expected_output} for t in test_cases]
        results = run_user_code(code, formatted_cases)

        pass_count = sum(1 for r in results if r["passed"])
        fail_count = len(results) - pass_count
        score = pass_count * 10

        if run_type == "final":
            Submission.objects.update_or_create(
                user=user,
                challenge=challenge,
                defaults={
                    "score": score,
                    "status": "Accepted",
                    "code": code
                }
            )

            total_score = Submission.objects.filter(
                user=user,
                challenge__contest=contest
            ).aggregate(total=Sum('score'))['total'] or 0

            ContestParticipation.objects.update_or_create(
                user=user,
                contest=contest,
                defaults={
                    "total_score": total_score
                }
            )

        return JsonResponse({
            "results": results,
            "pass_count": pass_count,
            "fail_count": fail_count,
            "score": score
        })

    except Challenge.DoesNotExist:
        return JsonResponse({"error": "Challenge not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e), "trace": traceback.format_exc()}, status=500)


#  contests/views.py
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_contest_challenges(request, contest_id):
    cache_key = f"contest_challenges_{contest_id}"
    data = cache.get(cache_key)

    if data:
        return Response(data)

    try:
        contest = Contest.objects.get(id=contest_id)
        contest_challenges = ContestChallenge.objects.filter(contest=contest).select_related('challenge')
        challenges = [cc.challenge for cc in contest_challenges]
        serializer = ChallengeSerializer(challenges, many=True, context={'request': request})
        data = serializer.data
        cache.set(cache_key, data, timeout=300)
        return Response(data)
    except Contest.DoesNotExist:
        return Response({"error": "Contest not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
