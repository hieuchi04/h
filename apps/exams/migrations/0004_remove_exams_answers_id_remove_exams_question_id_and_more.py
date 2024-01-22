# Generated by Django 5.0.1 on 2024-01-21 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_exams_exam_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exams',
            name='answers_id',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='question_id',
        ),
        migrations.RemoveField(
            model_name='exams',
            name='subject_id',
        ),
        migrations.AlterField(
            model_name='result',
            name='exam_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exams.exams'),
        ),
    ]
