from rest_framework import viewsets
from user.models import Student
from .serializers import StudentSerializer
from ..permissions import IsAdminOrTeacherViewingTheirStudents

class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrTeacherViewingTheirStudents]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Student.objects.all()
        elif hasattr(user, 'teacher'):
            return Student.objects.filter(
                studentgroup__group__teacher=user.teacher
            ).distinct()
        elif hasattr(user, 'student'):
            return Student.objects.filter(pk=user.student.pk)
        return Student.objects.none()