from rest_framework import serializers
from system import models as system_models
from drf_writable_nested import WritableNestedModelSerializer


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = system_models.RoleModel
        fields = '__all__'

    def create(self, validated_data):
        self.data


class UserSerializer(WritableNestedModelSerializer):
    class Meta:
        model = system_models.UserModel
        fields = '__all__'


class ListUserSerializer(UserSerializer):
    password = serializers.CharField(write_only=True)
    role = RoleSerializer(many=True)
