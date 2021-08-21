# we put our services that does not related to our model
from rest_framework.generics import get_object_or_404

from accounts.models import Account


def check_amount(data):
    source_account = data.get('transfer_source')
    transfer_amount = data.get('transfer_amount')
    destination_account = data.get('transfer_destination')

    source = get_object_or_404(Account.objects, pk=source_account.id)
    destination = get_object_or_404(Account.objects, pk=destination_account.id)

    source_amount = source_account.amount
    # if transfer_amount < source_amount:
    #     return True
    return True if transfer_amount < source_amount else False

