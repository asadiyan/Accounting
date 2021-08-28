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

    def validate(self, data):
        if data.get('transfer_source').bank_id == data.get('transfer_destination').bank_id:
            raise serializers.ValidationError('Operation is impossible! source and destination is same!')
        elif data.get('transfer_source').amount <= data.get('transfer_amount'):
            raise serializers.ValidationError('Account balance is not enough')
        return data

    class Meta:
        model = History
        fields = ['transfer_source', 'transfer_destination', 'transfer_amount']
        validators = []


class AccountWithdrawSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data.get('transfer_source').amount <= data.get('transfer_amount'):
            raise serializers.ValidationError('Account balance is not enough')

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
        return None
