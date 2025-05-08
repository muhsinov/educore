from rest_framework import serializers
from api.student.serializers import StudentSerializer
from api.group.serializers import GroupSerializer 
from group.models import StudentGroup

class StudentCourseSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)
    student = StudentSerializer(read_only=True)
    class Meta:
        model = StudentGroup
        fields = '__all__'
