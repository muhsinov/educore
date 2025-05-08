from rest_framework import serializers
from homework.models import Homework
from api.lesson.serializers import LessonSerializer

class HomeworkSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)
    class Meta:
        model = Homework
        fields = '__all__'