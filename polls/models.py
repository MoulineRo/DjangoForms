from django.db import models


class TeachersM(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    # birthday = models.IntegerField(max_length=10)
    birthday1 = models.IntegerField(default=4)
    birthday2 = models.IntegerField(default=4)
    birthday3 = models.IntegerField(default=4)
    theme = models.CharField(max_length=100)


class GroupM(models.Model):
    name = models.CharField(max_length=100)
