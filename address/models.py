from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=64)
    destrict = models.CharField(max_length=64)
    region = models.CharField(max_length=64)
    
