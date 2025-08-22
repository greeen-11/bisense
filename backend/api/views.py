# api/views.py
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer

class UserList(generics.ListCreateAPIView):  # supports GET + POST
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [AllowAny]