from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Or the correct model you're using

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User  # replace with your actual user model
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']
