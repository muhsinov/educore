# user/views.py
from rest_framework import generics
from user.models import User
from .serializers import UserCreateSerializer
from ..permissions import IsAdminUser

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsAdminUser]
