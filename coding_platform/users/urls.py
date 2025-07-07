from . import views 
from django.urls import path
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('profile/', views.profile, name='profile'),
    path('resend-otp/', views.resend_otp, name='resend_otp'),
    path('', views.dashboard_view, name='dashboard'),

]
