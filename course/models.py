from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=4)
    number = models.PositiveSmallIntegerField()
    
    # Validates that two courses with the same name and number cannot exist
    def clean(self):
        super().clean()
        existing_courses = Course.objects.filter(name=self.name, number=self.number)
        if self.pk:  # If the instance is being updated
            existing_courses = existing_courses.exclude(pk=self.pk)
        if existing_courses.exists():
            raise ValidationError("A course with this name and number already exists.")

    def full_name(self):
        return f"{self.name}{self.number}"

    def __str__(self):
        return self.full_name()

