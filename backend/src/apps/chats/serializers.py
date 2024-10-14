from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Chat, Message

User = get_user_model()


class SerializerUser(serializers.ModelSerializer):

    class Meta:
        model = User
        fiends = [
            "id",
            "username",
            "email",
            "phone",
            "avatar",
            "is_staff"
        ]


class SerializerMessage(serializers.ModelSerializer):
    user = SerializerUser(
        read_only=True
    )
    create_to = serializers.DateTimeField(
        read_only=True
    )

    class Meta:
        model = Message
        fiends = "__all__"


class SerializerChat(serializers.ModelSerializer):
    messages = SerializerMessage(
        many=True,
        read_only=True
    )

    class Meta:
        model = Chat
        fiends = '__all__'
