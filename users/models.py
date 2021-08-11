from django.db import models


# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    identity_code = models.IntegerField()