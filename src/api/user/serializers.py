from user.models import User, Student, Teacher
from rest_framework import serializers

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone', 'first_name', 'last_name', 'birth_date', 'address', 'role', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        role = validated_data.get("role")
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        if role == "student":
            Student.objects.create(user=user)
        elif role == "teacher":
            Teacher.objects.create(user=user, salary=0.00) 

        return user
