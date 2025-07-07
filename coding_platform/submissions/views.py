from rest_framework.decorators import api_view
from rest_framework.response import Response
from challenges.models import Challenge
from submissions.models import Submission

@api_view(['POST'])
def submit_code(request, challenge_id):
    try:
        if not request.user.is_authenticated:
            return Response({"error": "User not authenticated"}, status=401)

        code = request.data.get("code", "").strip()
        if not code:
            return Response({"error": "Empty code!"}, status=400)

        challenge = Challenge.objects.get(id=challenge_id)

        Submission.objects.create(
            user=request.user,
            challenge=challenge,
            code=code,
            status='Pending',  # Let admin review
            score=0
        )

        return Response({"message": "Submission stored successfully! Awaiting review."})

    except Challenge.DoesNotExist:
        return Response({"error": "Challenge not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
