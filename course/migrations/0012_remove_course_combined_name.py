# Generated by Django 5.0.1 on 2024-02-15 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_alter_course_combined_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='combined_name',
        ),
    ]
