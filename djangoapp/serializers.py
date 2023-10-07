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
    id_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    id_lab = serializers.PrimaryKeyRelatedField(queryset=Lab.objects.all()) 
    class Meta:
        model = ResLab
        fields = "__all__"
