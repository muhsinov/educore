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
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    text = models.TextField()
    file = models.FileField(upload_to='homeworks/',null=False,blank=False)
    grade = models.IntegerField(null=False,blank=False)
    teacher_advice = models.TextField()
    sended_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.student} - {self.homework}"






