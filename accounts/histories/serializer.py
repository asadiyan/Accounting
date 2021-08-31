from rest_framework import serializers

from .models import History


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['created_time', 'transfer_amount', 'transfer_source', 'transfer_destination']


class HistoryListSerializer(serializers.ModelSerializer):
    transfer_source = serializers.SerializerMethodField()
    transfer_destination = serializers.SerializerMethodField()

    class Meta:
        model = History
        fields = ['id', 'created_time', 'transfer_amount', 'transfer_source', 'transfer_destination', 'account_amount']

    def get_transfer_destination(self, obj):
        if obj.transfer_destination:
            return {'full_name': obj.transfer_destination.customer.get_full_name(),
                    'bank_name': obj.transfer_destination.bank.name,
                    'account_id': obj.transfer_destination.id
                    }
        return None

    def get_transfer_source(self, obj):
        if obj.transfer_source:
            return{"full_name": obj.transfer_source.customer.get_full_name(),
                   "bank_name": obj.transfer_source.bank.name,
                   "account_id": obj.transfer_source.id
                   }
        return None
