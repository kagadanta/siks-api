from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import Customer, Supplier


class UserSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()

    def get_status(self, obj):
        return {
            'is_staff': obj.is_staff,
            'is_superuser': obj.is_superuser,
            'is_active': obj.is_active
        }

    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'full_name',
            'status',
            'is_superuser',
            'is_staff',
            'is_active',
        ]


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)
    confirm = serializers.CharField(max_length=100)
    is_superuser = serializers.BooleanField()
    is_staff = serializers.BooleanField()
    is_active = serializers.BooleanField()

    def validate(self, data):
        if data['password'] != data['confirm']:
            raise serializers.ValidationError("Password tidak sama!")
        return data


class StatusUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'is_superuser',
            'is_staff',
            'is_active',
        ]

class SigninSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, required=True)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ['is_publish', 'numcode']


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100)
    confirm = serializers.CharField(max_length=100)

    def validate(self, data):
        if data['password'] != data['confirm']:
            raise serializers.ValidationError("Password tidak sama!")
        return data
