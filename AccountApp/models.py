from django.db import models
from UserApp.models import User
from BankApp.models import Bank
# Create your models here.


class Account(models.Model):
    account_user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    account_amount = models.IntegerField()
    account_created_time = models.DateTimeField(auto_now_add=True)
    account_bank_id = models.ForeignKey(Bank, on_delete=models.PROTECT)
    account_modified = models.DateTimeField()
