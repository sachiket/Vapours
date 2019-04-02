from django.db import models
from django.contrib import auth
from django.forms.widgets import RadioSelect
from django.urls import reverse
# Create your models here.

class User(auth.models.User,auth.models.PermissionsMixin,models.Model):
    name=models.CharField(max_length=55)
    TYPE_SELECT = (('0', 'Female'),('1', 'male'),)
    gender=models.CharField(max_length=11,choices=TYPE_SELECT)


    def __str__(self):
        return "@{}".format(self.username)
