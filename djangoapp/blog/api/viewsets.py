from rest_framework import viewsets
from .serializers import userSerializers
from django.contrib.auth import get_user_model
User = get_user_model()


class userviewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializers