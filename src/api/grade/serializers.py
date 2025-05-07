from rest_framework import serializers
from lesson.models import Grade
from api.lesson.serializers import LessonSerializer
from api.student.serializers import StudentSerializer

class GradeSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)
    student = StudentSerializer(read_only=True)
    class Meta:
        model = Grade
        fields = '__all__'