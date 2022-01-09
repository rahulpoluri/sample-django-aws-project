from django.db import models

# Create your models here.

class teachers1(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    comments = models.TextField(max_length=100)

class students1(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    comments = models.TextField(max_length=100)

class teachers(models.Model):
    pass

class students(models.Model):
    pass