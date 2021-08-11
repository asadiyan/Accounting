from django.db import models
from AccountApp.models import Account

# Create your models here.


class History(models.Model):
    history_date = models.DateTimeField(auto_now_add=True)
    history_transaction_amount = models.IntegerField()
    history_transaction_source_account = models.ForeignKey(Account, on_delete=models.PROTECT)
    history_transaction_destination_account = models.ForeignKey(Account, on_delete=models.PROTECT)
