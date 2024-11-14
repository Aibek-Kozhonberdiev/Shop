from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class SetUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=False,
        allow_null=False,
        validators=[validate_password]
    )
    avatar = serializers.ImageField(required=False, allow_null=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    email_confirmed = serializers.BooleanField(read_only=True)
    phone_confirmed = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "phone",
            "avatar",
            "is_staff",
            "is_active",
            "email_confirmed",
            "phone_confirmed",
        ]


class GoogleSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()
    username = serializers.CharField()
