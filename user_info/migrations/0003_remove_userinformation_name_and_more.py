# Generated by Django 5.0.1 on 2024-02-15 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0002_alter_userinformation_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinformation',
            name='name',
        ),
        migrations.AddField(
            model_name='userinformation',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userinformation',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
