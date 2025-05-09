from rest_framework import views
from lesson.models import Lesson
from lesson.serializers import LessonSerializer

class LessonViews(views.ModelViews):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer