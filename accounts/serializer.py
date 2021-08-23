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
    transfer_source = serializers.SerializerMethodField()
    transfer_destination = serializers.SerializerMethodField()

    class Meta:
        model = History
        fields = ['created_time', 'transfer_amount', 'transfer_source', 'transfer_destination', 'account_amount']

    def get_transfer_destination(self, obj):
        if obj.transfer_destination:
            return {"full_name": obj.transfer_destination.customer.get_full_name(),
                    "account_id": obj.transfer_destination.id
                    }
        return None

    def get_transfer_source(self, obj):
        if obj.transfer_source:
            return{"full_name": obj.transfer_source.customer.get_full_name(),
                   "account_id": obj.transfer_source.id
                   }
