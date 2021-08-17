from rest_framework import serializers

from rest_framework.decorators import action

from histories.models import History
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['customer', 'amount', 'created_time', 'bank', 'modified_time']


class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['amount', 'bank']


class AccountTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = ['transfer_source', 'transfer_destination', 'transfer_amount']


