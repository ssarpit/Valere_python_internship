from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .models import Contest

User = get_user_model()

@shared_task
def send_contest_submission_email(user_id, contest_id):
    try:
        user = User.objects.get(id=user_id)
        contest = Contest.objects.get(id=contest_id)
        send_mail(
            subject="✅ Contest Submission Confirmation",
            message=f"Hi {user.username},\n\nYou successfully submitted the contest: {contest.title}.\n\nBest of luck!",
            from_email="noreply@yourplatform.com",
            recipient_list=[user.email],
            fail_silently=False,
        )
    except Exception as e:
        print(f"Email send failed: {e}")
