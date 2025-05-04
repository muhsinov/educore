from django.db import models
from course.models import StudentCourse


class Payment(models.Model):
    student_couse = models.ForeignKey(StudentCourse, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.Choices()
    payment_date = models.DateField(auto_now_add=True)