from django.db import models

# Create your models here.


class Bank(models.Model):
    name = models.CharField(max_length=30)