from rest_framework import serializers
from .models import User, Lab, ResLab


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = "__all__"


class ResLabSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResLab
        fields = "__all__"
