from django.db import models

from educore.src.group.models import Group
from educore.src.user.models import Student


class Course(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    cost = models.IntegerField(null=False, blank=False)
    duration = models.IntegerField(null=False, blank=False)
    

    def __str__(self):
        return self.name


class StudentCourse(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.group_id} - {self.student_id}'

# for test changes