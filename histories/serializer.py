from rest_framework import serializers

from .models import History


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['created_time', 'transfer_amount', 'transfer_source', 'transfer_destination']

