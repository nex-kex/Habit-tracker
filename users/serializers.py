from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser


class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone"]
        extra_kwargs = {
            "email": {"required": False},
            "phone": {"required": False},
        }

    @staticmethod
    def validate_password(password):
        validate_password(password)
        return password


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "phone"]
