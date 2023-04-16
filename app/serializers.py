from rest_framework.serializers import ModelSerializer
from app.models import ToDo


class ToDoModelSerializer(ModelSerializer):

    class Meta:
        model = ToDo
        exclude = ()