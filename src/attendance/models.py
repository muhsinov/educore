from django.db import models
from lesson.models import Lesson
from user.models import Student




class Attendance(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.student} - {self.lesson}"


