from django.db import models
from users.models import Customer
from banks.models import Bank


# Create your models here.


class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    amount = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT, unique=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.bank.name} : {self.customer.username}'
