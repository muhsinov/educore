from rest_framework import serializers
from group.models import Group

from api.course.serializers import CourseSerializer

class GroupSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    class Meta:
        model = Group
        fields = '__all__'