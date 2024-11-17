from rest_framework import serializers

from .models import Chat, Message
from ..users.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    is_read = serializers.BooleanField(read_only=True)


    class Meta:
        model = Message
        fields = "__all__"


class ChatSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(read_only=True, many=True, source='users')
    messages = MessageSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Chat
        fields = "__all__"
