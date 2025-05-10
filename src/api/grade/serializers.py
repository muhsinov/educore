from rest_framework import serializers
from lesson.models import Grade
from api.lesson.serializers import LessonSerializer
from api.student.serializers import StudentSerializer

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'