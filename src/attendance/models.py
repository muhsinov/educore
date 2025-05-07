from django.db import models
from user.models import Student, Teacher
from lesson.models import Lesson

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='attendances')
    status = models.CharField(max_length=10, choices=[('late', 'Late'),('present', 'Present'), ('absent', 'Absent')])
    time = models.TimeField(auto_now_add=True)
    
    
    