from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=64,null=False,blank=False)
    destrict = models.CharField(max_length=64)
    region = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.street} {self.destrict} {self.region}"
