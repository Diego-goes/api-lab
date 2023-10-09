from rest_framework import serializers
from .models import User, Lab, Res_Lab


class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class Lab_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = "__all__"


class Res_Lab_Serializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    lab_id = serializers.PrimaryKeyRelatedField(queryset=Lab.objects.all()) 
    class Meta:
        model = Res_Lab
        fields = "__all__"
