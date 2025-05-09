from rest_framework import serializers
from homework.models import StudentHomework
from api.homework.serializers import HomeworkSerializer
from api.student.serializers import StudentSerializer

class StudentHomeworkSerializer(serializers.ModelSerializer):
    homework = HomeworkSerializer(read_only=True)
    student = StudentSerializer(read_only=True)
    class Meta:
        model = StudentHomework
        fields = '__all__'