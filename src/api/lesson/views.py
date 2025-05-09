from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from lesson.models import Lesson
from .serializers import LessonSerializer
from ..permissions import IsAdminOrReadOnly

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'teacher'):
            return Lesson.objects.filter(teacher=user.teacher)
        elif hasattr(user, 'student'):
            return Lesson.objects.filter(group__studentgroup__student=user.student)
        return Lesson.objects.none()