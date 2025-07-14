from django.shortcuts import render, redirect
from django.contrib.auth import  login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from datetime import datetime
from contests.models import Contest
from .models import UserProfile
from .forms import RegisterForm
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .tasks import send_email_task


# Register view, with OTP generation and email sending
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            dob = form.cleaned_data['dob']
            phone = form.cleaned_data['phone']
            gender = form.cleaned_data['gender']

            otp = get_random_string(length=6, allowed_chars='1234567890')

            request.session['otp'] = otp
            request.session['otp_timestamp'] = datetime.now().isoformat()
            request.session['pending_user'] = {
                'username': username,
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'dob': str(dob),
                'phone': phone,
                'gender': gender,
            }
            request.session['password_for_otp'] = password

            send_email_task.delay(email, otp, username)

            messages.info(request, "OTP sent to your email. Please verify to complete registration.")
            return redirect('verify_otp')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})





# OTP Verification View
def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get("otp")
        session_otp = request.session.get("otp")
        otp_time_str = request.session.get("otp_timestamp")
        user_data = request.session.get("pending_user")
        password = request.session.get("password_for_otp")

# Check if OTP expired
        if otp_time_str:
            otp_time = datetime.fromisoformat(otp_time_str)
            if (datetime.now() - otp_time).total_seconds() > 300:
                messages.error(request, "OTP has expired. Please register again.")
                return redirect('register')

        if entered_otp == session_otp and user_data and password:
            user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password=password,
                first_name=user_data['first_name'],
                last_name=user_data['last_name']
            )
            user.is_active = True
            user.save()

            UserProfile.objects.create(
                user=user,
                dob=user_data['dob'],
                phone=user_data['phone'],
                gender=user_data['gender']
            )

            login(request, user)

            for key in ['otp', 'otp_timestamp', 'pending_user', 'password_for_otp']:
                request.session.pop(key, None)

            messages.success(request, "Your email is verified. Welcome!")
            return redirect('login')

        return render(request, "users/verify_otp.html", {"error_message": "Invalid OTP"})
    
    return render(request, "users/verify_otp.html")

@permission_classes([IsAuthenticated])
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')


@login_required
def profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)

    if request.method == 'POST' and request.FILES.get('profile_image'):
        profile.profile_image = request.FILES['profile_image']
        profile.save()
        return redirect('profile')

    return render(request, "users/profile.html", {"user": user, "profile": profile})


def resend_otp(request):
    user_data = request.session.get("pending_user")
    if user_data:
        otp = get_random_string(length=6, allowed_chars='1234567890')
        request.session['otp'] = otp
        request.session['otp_timestamp'] = datetime.now().isoformat()
        send_email_task(user_data['email'], otp, user_data['username'])
        messages.success(request, "OTP resent successfully.")
    return redirect('verify_otp')

@permission_classes([IsAuthenticated])
@login_required
def dashboard_view(request):
    profile = UserProfile.objects.get(user=request.user)
    contests = Contest.objects.all()  # or filter for upcoming
    return render(request, 'users/dashboard.html', {
        'profile': profile,
        'contests': contests
    })

@permission_classes([IsAuthenticated])
def landing_view(request):
    return render(request, 'landing.html')