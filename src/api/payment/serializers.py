from rest_framework import serializers
from payment.models import Payment
from api.student_course.serializers import StudentCourseSerializer

class PaymentSerializer(serializers.ModelSerializer):
    student_course = StudentCourseSerializer(read_only=True)
    class Meta:
        model = Payment
        fields = '__all__'