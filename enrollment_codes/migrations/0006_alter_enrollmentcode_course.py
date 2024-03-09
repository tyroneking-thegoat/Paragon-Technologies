# Generated by Django 5.0.1 on 2024-03-09 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_remove_course_enrollcode_course_enroll_codes'),
        ('enrollment_codes', '0005_alter_enrollmentcode_enrollcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollmentcode',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment_codes', to='course.course'),
        ),
    ]
