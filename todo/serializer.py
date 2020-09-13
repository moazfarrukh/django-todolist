from rest_framework.serializers import ModelSerializer
from .models import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "text", "author", "done"]


class TodoUpdateSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ["done"]
