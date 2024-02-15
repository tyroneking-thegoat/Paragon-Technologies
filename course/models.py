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
        if Course.objects.filter(name=self.name, number=self.number).exists():
            raise ValidationError("A course with this name and number already exists.")

    def save(self, *args, **kwargs):
        self.clean()
        characters = string.ascii_letters + string.digits
        self.enrollCode = ''.join(random.choice(characters) for _ in range(5))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}{self.number}"