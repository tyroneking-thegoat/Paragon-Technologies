# Generated by Django 5.0.1 on 2024-03-09 22:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment_codes', '0002_rename_code_enrollmentcode_enrollcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollmentcode',
            name='EnrollCode',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]
