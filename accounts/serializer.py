from rest_framework import serializers

from accounts.histories.models import History
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

    @staticmethod
    def validate(data):
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

    @staticmethod
    def validate(data):
        if data.get('transfer_source').amount <= data.get('transfer_amount'):
            raise serializers.ValidationError('Account balance is not enough')
        return data

    class Meta:
        model = History
        fields = ['transfer_source', 'transfer_amount']


class AccountDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['transfer_destination', 'transfer_amount']


class AccountListSerializer(serializers.ModelSerializer):
    bank = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ['id', 'customer', 'amount', 'created_time', 'bank', 'modified_time']

    @staticmethod
    def get_bank(obj):
        return {'bank_name': obj.bank.name,
                'bank_id': obj.bank.id
                }


class AccountHistoryListSerializer(serializers.ModelSerializer):
    transfer_source = serializers.SerializerMethodField()
    transfer_destination = serializers.SerializerMethodField()

    class Meta:
        model = History
        fields = ['id', 'created_time', 'transfer_amount', 'transfer_source', 'transfer_destination', 'account_amount']

    @staticmethod
    def get_transfer_destination(obj):
        if obj.transfer_destination:
            return {'full_name': obj.transfer_destination.customer.get_full_name(),
                    'bank_name': obj.transfer_destination.bank.name,
                    'account_id': obj.transfer_destination.id
                    }
        return None

    @staticmethod
    def get_transfer_source(obj):
        if obj.transfer_source:
            return{"full_name": obj.transfer_source.customer.get_full_name(),
                   "bank_name": obj.transfer_source.bank.name,
                   "account_id": obj.transfer_source.id
                   }
        return None
