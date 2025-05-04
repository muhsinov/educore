from random import choices

from django.db import models
from user.models import Student



class Grade(models.Model):
    grade_types = [
        (3,'pass'),
        (4,'merit'),
        (5,'distinction')
    ]
    lesson = models.ForeignKey('Lesson',on_delete=models.CASCADE)
    student = models.ForeignKey('Student',on_delete=models.CASCADE)
    grade = models.IntegerField(choices=grade_types,default=3)
