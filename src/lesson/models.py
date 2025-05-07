from django.db import models
from user.models import Student
from user.models import Teacher
from group.models import Group




class Lesson(models.Model):
    name = models.CharField(max_length=64,null=False,blank=False)
    description = models.TextField()
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    room = models.CharField(max_length=64,null=False,blank=False)
    file = models.FileField(upload_to='lessons/')
    start_time = models.TimeField(null=False,blank=False)
    end_time = models.TimeField(null=False,blank=False)


    def __str__(self):
        return self.name




class Grade(models.Model):
    grade_types = [
<<<<<<< HEAD
        (0, "not graded"),
        (2, "rejected"),
        (3, 'pass'),
        (4, 'merit'),
        (5, 'distinction')
=======
        (0,"not graded"),
        (2,"rejected"),
        (3,'pass'),
        (4,'merit'),
        (5,'distinction')
>>>>>>> ab393175bc4f0eeb819ce40d99175a4032ab8227
    ]
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    grade = models.IntegerField(choices=grade_types,default=3)

    def __str__(self):
        return f"{self.student} - {self.lesson}: {self.grade}"