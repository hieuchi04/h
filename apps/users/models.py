from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomerUser(AbstractUser):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length= 15)
    
    def __str__(self):
        return self.username