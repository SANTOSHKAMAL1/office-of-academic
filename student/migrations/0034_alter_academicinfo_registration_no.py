# Generated by Django 5.1.7 on 2025-03-20 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0033_alter_academicinfo_registration_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='registration_no',
            field=models.IntegerField(default=222440, unique=True),
        ),
    ]
