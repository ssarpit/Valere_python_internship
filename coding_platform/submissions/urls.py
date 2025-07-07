from django.urls import path
from submissions.views import submit_code

urlpatterns = [
    path('submit/<int:challenge_id>/', submit_code, name='submit_code'),
]
