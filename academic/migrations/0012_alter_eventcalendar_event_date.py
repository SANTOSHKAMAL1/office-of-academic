# Generated by Django 5.1.6 on 2025-03-08 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0011_eventcalendar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcalendar',
            name='event_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
