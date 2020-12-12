from django.shortcuts import render
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from system import serializers as system_serializers
from system import models as system_models
from utils.defaultviewset import DefaultViewSet


class UserViewSet(DefaultViewSet):
    list_serializer = system_serializers.ListUserSerializer
    create_serializer = system_serializers.UserSerializer
    queryset = system_models.UserModel.objects.all().order_by('pk')


class RoleViewSet(ModelViewSet):
    serializer_class = system_serializers.RoleSerializer
    queryset = system_models.RoleModel.objects.all().order_by('pk')
