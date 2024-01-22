from django.db import models
from apps.exams.models import Exams
# Create your models here.

class Subjects(models.Model):
    subject_name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject_name


class Questions(models.Model):
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    question_text = models.TextField(default="", blank=False)
    active = models.BooleanField(default=True)
    exam_id = models.ForeignKey(Exams, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.question_text


class Answers(models.Model):
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_text = models.TextField(default='', blank=False)
    is_correct = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.answer_text