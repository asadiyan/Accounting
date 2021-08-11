from django.db import models
from accounts.models import Account

# Create your models here.


class History(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    transaction_amount = models.IntegerField()
    transaction_source = models.ForeignKey(Account, on_delete=models.PROTECT, null=True, related_name='source_account')
    transaction_destination = models.ForeignKey(Account, on_delete=models.PROTECT, null=True, related_name="destination_account")

