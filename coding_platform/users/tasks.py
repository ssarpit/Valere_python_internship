# users/tasks.py
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

import logging
logger = logging.getLogger(__name__)

@shared_task
def send_email_task(email, otp, uname):
    try:
        subject = "Email Verification - Coding Platform"
        from_email = settings.EMAIL_HOST_USER
        html_content = render_to_string('email/email_otp.html', {'user': uname, 'otp': otp})
        text_content = f"Hi {uname}, your OTP is: {otp}"

        msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        logger.info(f"✅ OTP email sent to {email}")
    except Exception as e:
        logger.error(f"❌ Failed to send OTP to {email}: {e}")
