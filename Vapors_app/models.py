from django.db import models
from django.contrib import auth
from django import forms
from django.urls import reverse
# Create your models here


class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)


# class Order(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
class BlogComments(models.Model):
    f1 = models.CharField(max_length=100)
    f2 = models.CharField(max_length=100)
    f3 = models.CharField(max_length=100)
    f4 = models.CharField(max_length=100)
    f5 = models.CharField(max_length=100)
    f6 = models.CharField(max_length=100)
    f7 = models.CharField(max_length=100)
    f8 = models.CharField(max_length=100)
    f9 = models.CharField(max_length=100)
    f10 = models.CharField(max_length=100)
    f11 = models.CharField(max_length=100)
    f12 = models.CharField(max_length=100)
    f13 = models.CharField(max_length=100)
    f14 = models.CharField(max_length=100)
    f15 = models.CharField(max_length=100)
    f16 = models.CharField(max_length=100)
    f17 = models.CharField(max_length=100)
    f18 = models.CharField(max_length=100)
    f19 = models.CharField(max_length=100)
    f20 = models.CharField(max_length=100)
    f21 = models.CharField(max_length=100)
    f22 = models.CharField(max_length=100)
    f23 = models.CharField(max_length=100)
    f24 = models.CharField(max_length=100)
    f25 = models.CharField(max_length=100)
    f26 = models.CharField(max_length=100)
    f27 = models.CharField(max_length=100)
