from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    roll = models.CharField(max_length=50,null=True,blank=True)
    subject = models.CharField(max_length=50,null=True,blank=True)
