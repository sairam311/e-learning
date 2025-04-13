from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'
        extra_kwargs = {
            'user_code': {'required': False},       # Generated in the view
            'referal_code': {'required': False},    # Optional
            'referal_email':{'required': False},
            'password': {'write_only': True},  #  This hides password in API responses
        }

    def validate_email(self, value):
        if students.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value
