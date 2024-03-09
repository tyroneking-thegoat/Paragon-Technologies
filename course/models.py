from django.db import models
from django.core.exceptions import ValidationError
import random
import string

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=4)
    number = models.PositiveSmallIntegerField()
    enrollCode = models.CharField(max_length=5, null=True, blank=True)
    
    #Validates that two courses with the same name and number cannot exist
    def clean(self):
        super().clean()
        existing_courses = Course.objects.filter(name=self.name, number=self.number)
        if self.pk:  # If the instance is being updated
            existing_courses = existing_courses.exclude(pk=self.pk)
        if existing_courses.exists():
            raise ValidationError("A course with this name and number already exists.")

    def save(self, *args, **kwargs):
        if not self.pk and not self.enrollCode:  # Check if the instance is being created for the first time and enrollCode is empty
            characters = string.ascii_letters + string.digits
            self.enrollCode = ''.join(random.choice(characters) for _ in range(5))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}{self.number}"