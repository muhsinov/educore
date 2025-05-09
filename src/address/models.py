from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=64,null=False,blank=False)
    destrict = models.CharField(max_length=64)
    region = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=64, null=True, blank=True)
    country = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return f"{self.street} {self.destrict} {self.region}"
    
    def __str__(self):
        return f"{self.street}, {self.destrict}, {self.region}"
