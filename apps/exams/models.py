from django.db import models
from datetime import timedelta 
from apps.users.models import CustomerUser
# Create your models here.

class Exams(models.Model):
    exam_name = models.CharField(max_length=255, default= " ")
    user_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    time_limit = models.DurationField(default= timedelta(minutes=60))
    active = models.BooleanField(default=True)

    def __str__(self) :
        return self.exam_name


class Result(models.Model):
    user_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    exam_id = models.OneToOneField(Exams, on_delete=models.CASCADE)
    time_finish = models.TimeField()
    score = models.IntegerField(default=0)
    active = models.BooleanField(default=True)