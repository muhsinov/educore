from rest_framework import serializers
from attendance.models import Attendance
from api.lesson.serializers import LessonSerializer
from api.student.serializers import StudentSerializer

class AttendanceSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    lesson = LessonSerializer(read_only=True)
    class Meta:
        model = Attendance
        fields = '__all__'
        read_only_fields = ['time']

