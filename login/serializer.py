from rest_framework import serializers
from .models import *


class Custom_serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class User_profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = User_profile
        fields = '__all__'
        