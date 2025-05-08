from rest_framework import serializers
from lesson.models import Lesson
from api.group.serializers import GroupSerializer

class LessonSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)
    class Meta:
        model = Lesson
        fields = '__all__'