# Generated by Django 5.0.1 on 2024-01-22 04:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_exams_question_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exams',
            name='question_id',
        ),
        migrations.AlterField(
            model_name='exams',
            name='time_limit',
            field=models.DurationField(default=datetime.timedelta(seconds=3600)),
        ),
    ]