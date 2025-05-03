from django.db import models
from django.contrib.auth.models import User
from group.models import Group



class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='lessons')
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='lessons')
    room = models.CharField(max_length=50)
    file = models.FileField(upload_to='lesson_files/',blank=True, null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name}({self.group.name})"