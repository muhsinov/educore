from django.db import models
from course.models import Course



class Group(models.Model):
    name = models.CharField(max_length=64)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    room = models.CharField(max_length=64)
    started_at = models.DateField()
    end_at = models.DateField()
    
    def __str__(self):
        return f"{self.name} ({self.course.name})"