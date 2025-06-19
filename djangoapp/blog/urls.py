# Import necessary modules
from django.contrib import admin  # Django admin module
from django.urls import include,path       # URL routing
from blog.views import *  # Import views from the authentication app
from django.conf import settings   # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Static files serving
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

    

urlpatterns = [
    path('', include(router.urls)),
    path('', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('login/', views.login_view, name='login'),  # updated name
    path('home/', views.home, name='home'),
    path("logout/", LogoutView.as_view(next_page="/blog/login/"), name="logout"),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
]


# Serve media files if DEBUG is True (development mode)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # Serve static files using staticfiles_urlpatterns
# urlpatterns += staticfiles_urlpatterns()