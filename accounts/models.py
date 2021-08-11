from django.db import models
from users.models import User
from banks.models import Bank
# Create your models here.


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    amount = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    modified_time = models.DateTimeField()
