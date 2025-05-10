from rest_framework import viewsets
from course.models import Course
from .serializers import CourseSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission
from ..permissions import IsAdminOrReadOnly    


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]
