# Generated by Django 5.0.1 on 2024-02-15 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_number'),
        ('user_info', '0003_remove_userinformation_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course'),
        ),
    ]