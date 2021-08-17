from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Customer(AbstractUser):
    identity_code = models.CharField(max_length=10)
