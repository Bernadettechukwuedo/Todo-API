from rest_framework import serializers
from .models import Todo


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title", "description", "completed"]

    def create(self, validated_data, **kwargs):
        user = kwargs["user"]
        todo = super().create(dict(user=user, **validated_data))

        return todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
