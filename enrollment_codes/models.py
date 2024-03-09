# models.py

from django.db import models
from django.core.validators import RegexValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from course.models import Course  # Import Course model from the course app
import random
import string

class EnrollmentCode(models.Model):
    EnrollCode = models.CharField(max_length=5, unique=True, validators=[
        RegexValidator(r'^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.'),
        MaxLengthValidator(5)
    ], blank=True, null=True)  # Allow EnrollCode to be nullable
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def clean(self):
        super().clean()
        if self.EnrollCode is not None:  # Check if EnrollCode is provided
            existing_enrollment_codes = EnrollmentCode.objects.exclude(pk=self.pk).filter(EnrollCode=self.EnrollCode)
            if existing_enrollment_codes.exists():
                raise ValidationError("An enrollment code with this code already exists.")

    def save(self, *args, **kwargs):
        if not self.pk and self.EnrollCode is None:  # Check if the instance is being created for the first time and EnrollCode is empty
            characters = string.ascii_letters + string.digits
            self.EnrollCode = ''.join(random.choice(characters) for _ in range(5))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.EnrollCode} - {self.course}"