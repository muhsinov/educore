from django.db import models

<<<<<<< HEAD

=======
>>>>>>> ab393175bc4f0eeb819ce40d99175a4032ab8227
class Course(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    cost = models.IntegerField(null=False, blank=False)
    duration = models.IntegerField(null=False, blank=False)
    

    def __str__(self):
        return self.name

<<<<<<< HEAD



=======
>>>>>>> ab393175bc4f0eeb819ce40d99175a4032ab8227
