from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user', 'amount', 'created_time', 'bank', 'modified_time']


class AccountGetInfoSerializer(serializers.Serializer):
    user = serializers.CharField()
    amount = serializers.IntegerField()
    created_time = serializers.DateTimeField()
    bank = serializers.IntegerField()
    modified_time = serializers.DateTimeField()

    def get_user(self, obj):
        return obj.user

    def get_amount(self, obj):
        return obj.amount

    def get_created_time(self, obj):
        return obj.created_time

    def get_bank(self, obj):
        return obj.bank

    def get_modified_time(self, obj):
        return obj.modified_time


class AccountDepositSerializer(serializers.Serializer):
    # source_account =
    #
    # destination_account =

    amount = serializers.IntegerField()
    bank = serializers.CharField()