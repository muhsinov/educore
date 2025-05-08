from email.policy import default
from random import choices
from django.db import models
from lesson.models import Lesson
from user.models import Student


class Homework(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class StudentHomework(models.Model):
    grade_types = [
        (0, "not rejected"),
        (2, "rejected"),
        (3, 'pass'),
        (4, 'merit'),
        (5, 'distinction')
    ]
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    text = models.TextField()
    file = models.FileField(upload_to='homeworks/',null=False,blank=False)
    grade = models.IntegerField(choices=grade_types,default=3,null=False,blank=False)
    teacher_advice = models.TextField()
    sended_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.student} - {self.homework}"






