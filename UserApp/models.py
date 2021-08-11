from django.db import models


# Create your models here.

class User(models.Model):
    user_firstname = models.CharField(max_length=30)
    user_lastname = models.CharField(max_length=50)
    user_password = models.CharField(max_length=20)
    user_identity_code = models.IntegerField(max_length=10)