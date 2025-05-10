from rest_framework import viewsets
from user.models import Teacher
from .serializers import TeacherSerializer
from ..permissions import IsAdminOrSelf


class TeacherViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminOrSelf]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Teacher.objects.all()
        elif hasattr(user, 'student'):
            return Teacher.objects.filter(
                groups__studentgroup__student=user.student
            ).distinct()
        elif hasattr(user, 'teacher'):
            return Teacher.objects.filter(pk=user.teacher.pk)
        return Teacher.objects.none()