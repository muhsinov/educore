from django.db import models
from course.models import StudentCourse


class Payment(models.Model):
    pay_type = (
        (0, "Cash"),
        (1, "Card"),
        (3,"Electron pay")
    )
    student_couse = models.ForeignKey(StudentCourse, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=False,blank=False)
    type = models.IntegerField(choices=pay_type,default=0)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_couse} - {self.amount}"

