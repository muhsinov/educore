from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    cost = models.IntegerField(null=False, blank=False)
    duration = models.IntegerField(null=False, blank=False)
    

    def __str__(self):
        return self.name




