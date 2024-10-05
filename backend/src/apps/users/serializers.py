from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class SerializerSetUser(serializers.ModelSerializer):
    avatar = serializers.ImageField(
        required=False,
        allow_null=True
    )
    is_staff = serializers.BooleanField(
        read_only=True,
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone",
            "avatar",
            "is_staff"
        ]
