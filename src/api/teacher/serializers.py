from rest_framework import serializers
from user.models import Teacher

from api.user.serializers import UserSerializer

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Teacher
        fields = '__all__'