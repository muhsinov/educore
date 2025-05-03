from django.db import models
from lesson.models import Lesson
from user.models import User


class Homework(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='homeworks')
    deadline = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Lesson: {self.lesson.name})" 
    
class StudentHomework(models.Model):
    GRADE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='student_homework')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_homework')

    text = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='homeworks/', blank=True, null=True)

    grade = models.IntegerField(choices=GRADE_CHOICES, blank=True, null=True)
    teacher_advice = models.TextField(blank=True, null=True)
    sended_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.homework.name}"


