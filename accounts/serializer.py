from rest_framework import serializers

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


class AccountWithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['transfer_source', 'transfer_amount']


class AccountDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['transfer_source', 'transfer_amount']


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'customer', 'amount', 'created_time', 'bank', 'modified_time']


class AccountHistoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['created_time', 'transfer_amount', 'transfer_source', 'transfer_destination']
