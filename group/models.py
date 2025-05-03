from django.db import models
from course.models import Course

class Group(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='groups')
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.course.code})"

