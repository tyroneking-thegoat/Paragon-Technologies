# Generated by Django 5.0.1 on 2024-02-15 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_number'),
        ('user_info', '0006_remove_userinformation_course_userinformation_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='course',
            field=models.ManyToManyField(to='course.course'),
        ),
    ]
