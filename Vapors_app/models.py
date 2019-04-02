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
class Blog(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Friends = models.IntegerField()
    Gender = models.CharField(max_length=100)
    Sexuality = models.CharField(max_length=100)
    Body_weight = models.CharField(max_length=100)
    Virgin = models.CharField(max_length=100)
    Prostitution_legal = models.CharField(max_length=100)
    Pay_for_sex = models.CharField(max_length=100)    
    Social_fear = models.CharField(max_length=100)
    PHQ1A = models.CharField(max_length=100)
    PHQ1B = models.CharField(max_length=100)
    PHQ1C = models.CharField(max_length=100)
    PHQ1D = models.CharField(max_length=100)
    #f5  = models.CharField(max_length=100)
    PHQ9 = models.CharField(max_length=100)
    PHQ6A = models.CharField(max_length=100)
    PHQ6B = models.CharField(max_length=100)
    PHQ6C = models.CharField(max_length=100)
    PHQ6D = models.CharField(max_length=100)
    #f11 = models.CharField(max_length=100)
    PHQ2A = models.CharField(max_length=100)
    PHQ2B = models.CharField(max_length=100)
    PHQ2C = models.CharField(max_length=100)
    #f15 = models.CharField(max_length=100)
    PHQ3 = models.CharField(max_length=100)
    PHQ4A = models.CharField(max_length=100)
    PHQ4B = models.CharField(max_length=100)
    PHQ4C = models.CharField(max_length=100)
    #f20 = models.CharField(max_length=100)
    PHQ8 = models.CharField(max_length=100)
    PHQ5 = models.CharField(max_length=100)
    PHQ7A = models.CharField(max_length=100)
    PHQ7B = models.CharField(max_length=100)
    PHQ7C = models.CharField(max_length=100)
    PHQ7D = models.CharField(max_length=100)
    #f27 = models.CharField(max_length=100)
