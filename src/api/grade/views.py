from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from lesson.models import Grade
from .serializers import GradeSerializer
from ..permissions import IsTeacherOrReadOnly
from rest_framework.exceptions import PermissionDenied


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'teacher'):
            return Grade.objects.filter(lesson__teacher=user.teacher)
        elif hasattr(user, 'student'):
            return Grade.objects.filter(student=user.student)
        return Grade.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if hasattr(user, 'teacher'):
            lesson = serializer.validated_data['lesson']
            if lesson.teacher != user.teacher:
                raise PermissionDenied("Siz bu darsga baho qoya olmaysiz.")
        serializer.save()