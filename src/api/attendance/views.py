from rest_framework import viewsets
from attendance.models import Attendance
from .serializers import AttendanceSerializer
from ..permissions import AttendancePermission

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [AttendancePermission]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Attendance.objects.all()
        elif hasattr(user, 'teacher'):
            return Attendance.objects.filter(lesson__teacher=user.teacher)
        elif hasattr(user, 'student'):
            return Attendance.objects.filter(student=user.student)
        return Attendance.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if hasattr(user, 'teacher'):
            serializer.save()
