# Generated by Django 5.0.1 on 2024-02-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_course_combined_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='combined_name',
            field=models.CharField(default='', max_length=8, unique=True),
        ),
    ]
