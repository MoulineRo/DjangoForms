from django.db import models


class TeachersM(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birthday = models.DateField()
    theme = models.CharField(max_length=100)


class GroupM(models.Model):
    name = models.CharField(max_length=100)
