from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(User):
    identity_code = models.CharField(max_length=10)
