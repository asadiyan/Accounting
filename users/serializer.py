from rest_framework import serializers

from .models import Customer


# serializers are defined here

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
    identity_code = serializers.CharField()
    username = serializers.CharField()
    password = serializers.IntegerField()

    @staticmethod
    def get_first_name(obj):
        return obj.first_name

    @staticmethod
    def get_last_name(obj):
        return obj.last_name

    @staticmethod
    def get_identity_code(obj):
        return obj.identity_code

    @staticmethod
    def get_username(obj):
        return obj.username

    @staticmethod
    def get_password(obj):
        return obj.password
