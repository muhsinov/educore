# user/views.py
from rest_framework import generics
from user.models import User
from .serializers import UserCreateSerializer
from ..permissions import IsAdminUser

class UserCreateAPIView(generics.CreateAPIView, generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsAdminUser]

class UserGetAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        user = self.request.user
        if user.is_staff:
            return super().get_object()
        return user