from django.db import models

# Create your models here.


class Bank(models.Model):
    bank_name = models.CharField(max_length=30)