# ✅ views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from challenges.models import Challenge, TestCase
from submissions.models import Submission
from .utils import run_user_code
import traceback
from django.utils import timezone
from django.http import JsonResponse
from contests.models import ContestParticipation
from rest_framework.response import Response
from submissions.models import Submission
from django.db.models import Sum
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

        return Response({"message": "Submission stored successfully! Awaiting review."})

    except Challenge.DoesNotExist:
        return Response({"error": "Challenge not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def leaderboard(request):
    leaderboard = (
        ContestParticipation.objects
        .filter(has_submitted=True)
        .select_related('user', 'contest')
        .order_by('-total_score', 'time_taken_seconds')
        .values('user__username', 'total_score', 'time_taken_display')
    )
    return Response(list(leaderboard))
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def execute_code(request, challenge_id):
    try:
        code = request.data.get("code", "")
        run_type = request.GET.get("type", "test")
        user = request.user

        challenge = Challenge.objects.get(id=challenge_id)

        test_cases = TestCase.objects.filter(challenge=challenge)
        if run_type == "test":
            test_cases = test_cases.filter(is_hidden=False)

        formatted_cases = [{"input": t.input, "expected_output": t.expected_output} for t in test_cases]
        results = run_user_code(code, formatted_cases)

        pass_count = sum(1 for r in results if r["passed"])
        fail_count = len(results) - pass_count
        score = pass_count * 10

        if run_type == "final":
            # ✅ Save submission
            Submission.objects.update_or_create(
                user=user,
                challenge=challenge,
                defaults={
                    "score": score,
                    "status": "Accepted",
                    "code":code
                    # optionally save latest code
                }
            )

            # ✅ Update total score in ContestParticipation
            from contests.models import ContestParticipation

            contest = challenge.contest  # ✅ Ensure Challenge has contest FK

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
