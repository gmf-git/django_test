from rest_framework import serializers

from notes import models as notes_model
from system.serializers import ListUserSerializer


class NotesSerializer(serializers.ModelSerializer):
    user = ListUserSerializer(read_only=True)
    time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = notes_model.Notes
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data.setdefault('user', user)
        return super().create(validated_data)
