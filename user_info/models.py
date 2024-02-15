from django.db import models
from course.models import Course
from django.contrib.auth.models import User

class userInformation(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField()
    course = models.ManyToManyField(Course)
    name = models.CharField(max_length=20, default=username)

    class Meta:
        db_table = 'User Information'
        verbose_name = 'User Information'
        verbose_name_plural = 'User Information'

    def __str__(self):
        return self.name