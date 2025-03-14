
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User

# Create your models here.

class Users(AbstractUser):
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    balance = models.FloatField(default=0.00, null=True)
    block = models.BooleanField(default=False)
    gender = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='picture', blank=True, null=True)

    def __str__(self):
        return self.username
    
