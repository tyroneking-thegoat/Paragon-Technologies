from django.db import models
from course.models import Course

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=4)
    number = models.PositiveSmallIntegerField()
    fkey = models.ForeignKey(Course)