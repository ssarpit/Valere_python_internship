from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.crypto import get_random_string
from django.conf import settings
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from .models import CustomUser

def generate_random_alphanumeric(length):
    return get_random_string(length)

def send_email(email, otp, uname):
    subject = "Email Verification and Account Activation"
    from_email = settings.EMAIL_HOST_USER
    to_email = [email]
    context = {
        'user': uname,
        'otp': otp
    }

    html_content = render_to_string('email/otp_email.html', context)
    text_content = f"Hi {uname},\nYour OTP is: {otp}. It is valid for 5 minutes.\nPlease do not share this code."

    email_message = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email_message.attach_alternative(html_content, "text/html")
    email_message.send()
@login_required
def home(request):
    return render(request, "blog/home.html")

def welcome(request):
    return render(request, "blog/welcome.html")

def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        dob = request.POST["dob"]
        gender = request.POST["gender"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        password = request.POST["password"]

        if CustomUser.objects.filter(email=email).exists():
            return render(request, "blog/register.html", {
                "error_message": "Email already registered."
            })

        otp = generate_random_alphanumeric(6)
        send_email(email, otp, name)

        request.session['pending_user'] = {
            "name": name,
            "dob": dob,
            "gender": gender,
            "phone": phone,
            "email": email,
            "password": password,
        }
        request.session['otp'] = otp

        return redirect('verify_otp')

    return render(request, "blog/register.html")

def verify_otp(request):
    if request.method == "POST":
        entered_otp = request.POST.get("otp")
        session_otp = request.session.get("otp")
        pending_user = request.session.get("pending_user")

        if entered_otp == session_otp and pending_user:
            user = CustomUser.objects.create_user(
                username=pending_user['email'],
                email=pending_user['email'],
                password=pending_user['password'],
                first_name=pending_user['name'],
                dob=pending_user['dob'],
                gender=pending_user['gender'],
                phone_number=pending_user['phone']
            )
            user.save()

            del request.session['pending_user']
            del request.session['otp']

            login(request, user)
            return redirect("home")

        return render(request, "blog/verify_otp.html", {
            "error_message": "Invalid OTP. Please try again."
        })

    return render(request, "blog/verify_otp.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            return render(request, "blog/login.html", {
                "error_message": "Email and Password are required."
            })

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "blog/login.html", {
                "error_message": "Invalid email or password."
            })

    return render(request, "blog/login.html")

def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def profile(request):
    custom_user = CustomUser.objects.all().filter(email=request.user)
    print(custom_user)
    if request.method == 'POST' and request.FILES.get('profile_image'):
        custom_user.profile_image = request.FILES['profile_image']
        # custom_user.save()
        return redirect('profile')

    return render(request, 'blog/profile.html', {'user': custom_user})
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'blog/change_password.html', {'form': form})



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer