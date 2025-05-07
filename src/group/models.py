from django.db import models
from course.models import Course
from user.models import Student



class Group(models.Model):
    objects = None
    name = models.CharField(max_length=64)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    room = models.CharField(max_length=64)
    started_at = models.DateField()
    end_at = models.DateField()
    
    def __str__(self):
        return f"{self.name} ({self.course.name})"
    
class StudentGroup(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.group_id} - {self.student_id}'