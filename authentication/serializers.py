from rest_framework import serializers
from authentication.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'password']


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email', 
            'first_name', 
            'last_name', 
            'phone_number', 
            'otp', 
            'otp_expiry', 
            'last_login', 
            'is_active',
            'is_phone_verified', 
            'is_email_verified', 
            'is_verified',
            ]


class VerifyOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.IntegerField()


class ResendOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
