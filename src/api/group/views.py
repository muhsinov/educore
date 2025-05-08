from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import GroupSerializer
from django.contrib.auth.models import Group

User = Group()

class GroupDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = GroupSerializer

    def get_object(self):
        return self.request.user
