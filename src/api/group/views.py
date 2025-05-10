from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from group.models import Group, StudentGroup
from .serializers import GroupSerializer, StudentGroupSerializer
from ..permissions import IsAdminOrReadOnly

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Group.objects.all()

        if user.role == 'teacher':
            return Group.objects.filter(teacher=user.teacher)

        if user.role == 'student':
            return Group.objects.filter(studentgroup__student_id=user.student)

        return Group.objects.none()


class StudentGroupViewSet(viewsets.ModelViewSet):
    serializer_class = StudentGroupSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return StudentGroup.objects.all()

        if hasattr(user, 'student'):
            return StudentGroup.objects.filter(student_id=user.student)

        return StudentGroup.objects.none()
