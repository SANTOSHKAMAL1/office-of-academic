# Generated by Django 5.1.6 on 2025-03-05 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0024_alter_academicinfo_registration_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='registration_no',
            field=models.IntegerField(default=219882, unique=True),
        ),
    ]
