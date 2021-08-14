from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'identity_code', 'username', 'password']


class CustomerLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class CustomerGetInfoSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    identity_code = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.IntegerField()

    def get_first_name(self, obj):
        return obj.first_name

    def get_last_name(self, obj):
        return obj.last_name

    def get_identity_code(self, obj):
        return obj.identity_code

    def get_username(self, obj):
        return obj.username

    def get_password(self, obj):
        return obj.password
