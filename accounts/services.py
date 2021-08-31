# we put our services that does not related to our model
from rest_framework.generics import get_object_or_404

from accounts.models import Account
from accounts.histories import History


def check_account(account):
    return True if get_object_or_404(Account.objects, pk=account.id) else False


def check_amount(data: object) -> object:
    source_account = data.get('transfer_source')
    transfer_amount = data.get('transfer_amount')
    return True if transfer_amount < source_account.amount else False


def do_transfer(data):
    amount = data.get('transfer_amount')
    source = data.get('transfer_source')
    destination = data.get('transfer_destination')
    if destination:
        source.amount = source.amount - amount
        destination.amount = destination.amount + amount
        destination.save()
        source.save()
        History.objects.create(transfer_amount=amount, transfer_source=source, transfer_destination=destination)
    else:
        # it needs to be implemented
        return
