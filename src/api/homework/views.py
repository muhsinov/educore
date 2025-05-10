from rest_framework import viewsets
from homework.models import Homework, StudentHomework
from .serializers import HomeworkSerializer, StudentHomeworkSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.utils import timezone

class HomeworkViewSet(viewsets.ModelViewSet):
    serializer_class = HomeworkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'teacher'):
            return Homework.objects.filter(lesson__teacher__user=user)
        elif hasattr(user, 'student'):
            return Homework.objects.filter(lesson__group__student__user=user).distinct()
        elif user.is_staff:
            return Homework.objects.all()
        return Homework.objects.none()

    def perform_create(self, serializer):
        if not hasattr(self.request.user, 'teacher'):
            raise PermissionDenied("Only teachers can create homework")
        serializer.save()

class StudentHomeworkViewSet(viewsets.ModelViewSet):
    serializer_class = StudentHomeworkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'teacher'):
            return StudentHomework.objects.filter(homework__lesson__teacher__user=user)
        elif hasattr(user, 'student'):
            return StudentHomework.objects.filter(student__user=user)
        elif user.is_staff:
            return StudentHomework.objects.all()
        return StudentHomework.objects.none()

    def perform_create(self, serializer):
        homework = serializer.validated_data['homework']
        if timezone.now() > homework.deadline:
            raise PermissionDenied("You cannot submit after the deadline")
        if not hasattr(self.request.user, 'student'):
            raise PermissionDenied("Only students can submit homework")
        serializer.save(student=self.request.user.student)

    def perform_update(self, serializer):
        if not hasattr(self.request.user, 'teacher'):
            raise PermissionDenied("Only teachers can grade student homework")
        serializer.save()