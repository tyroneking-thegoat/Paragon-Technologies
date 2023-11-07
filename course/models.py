from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=4)
    number = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.name + str(self.number)