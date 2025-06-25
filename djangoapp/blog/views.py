from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.crypto import get_random_string
from django.conf import settings
from rest_framework import viewsets
from .models import CustomUser
# from .serializers import BookSerializer

# Utility functions
def generate_random_alphanumeric(length):
    return get_random_string(length)

def send_email(email, otp, uname):
    subject = "Email Verification"
    from_email = settings.EMAIL_HOST_USER
    html_content = render_to_string('email/otp_email.html', {'user': uname, 'otp': otp})
    text_content = f"Hi {uname}, Your OTP is: {otp}"
    msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

# Views
def welcome(request):
    return render(request, "blog/welcome.html")

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not all([name, dob, gender, phone, email, password]):
            return render(request, "blog/register.html", {"error_message": "Please fill all fields."})

        if CustomUser.objects.filter(email=email).exists():
            return render(request, "blog/register.html", {"error_message": "Email already exists."})

        otp = generate_random_alphanumeric(6)
        try:
            send_email(email, otp, name)
        except Exception as e:
            return render(request, "blog/register.html", {"error_message": "Failed to send OTP email. Please try again."})

        # Store all but password in session (avoid plaintext password storage)
        request.session['pending_user'] = {
            "name": name, "dob": dob, "gender": gender,
            "phone": phone, "email": email
        }
        # Store OTP and hashed password separately or handle after verification
        request.session['otp'] = otp
        request.session['password_for_otp'] = password  # Ideally hash password or handle differently

        return redirect('verify_otp')

    return render(request, "blog/register.html")
def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get("otp")
        session_otp = request.session.get("otp")
        user_data = request.session.get("pending_user")
        password = request.session.get("password_for_otp")

        if entered_otp == session_otp and user_data and password:
            user = CustomUser.objects.create_user(
                username=user_data['email'], email=user_data['email'], password=password,
                first_name=user_data['name'], dob=user_data['dob'],
                gender=user_data['gender'], phone_number=user_data['phone']
            )
            user.backend = 'blog.backends.EmailBackend'
            login(request, user)
            # Clean session data
            for key in ['otp', 'pending_user', 'password_for_otp']:
                if key in request.session:
                    del request.session[key]
            return redirect('login')

        return render(request, "blog/verify_otp.html", {"error_message": "Invalid OTP"})

    return render(request, "blog/verify_otp.html")
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)  # will work if backend supports email login
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            return render(request, "blog/login.html", {"error_message": "Invalid credentials."})
    return render(request, "blog/login.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, "blog/home.html")

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST' and request.FILES.get('profile_image'):
        user.profile_image = request.FILES['profile_image']
        user.save()
        return redirect('profile')
    return render(request, "blog/profile.html", {"user": user})

@login_required
def change_password(request):
    form = PasswordChangeForm(request.user, request.POST or None)
    if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user)
        return redirect("profile")
    return render(request, "blog/change_password.html", {"form": form})
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer