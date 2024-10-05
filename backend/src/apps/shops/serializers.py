from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Shop, Complaint, Rating

User = get_user_model()


class SerializerRating(serializers.ModelSerializer):
    date_writing = serializers.DateTimeField(
        read_only=True
    )
    update_to = serializers.DateTimeField(
        read_only=True
    )

    class Meta:
        model = Rating
        fields = "__all__"


class SerializerShop(serializers.ModelSerializer):
    logo = serializers.ImageField(
        required=False
    )
    ban = serializers.BooleanField(
        read_only=True
    )
    number_of_complaints = serializers.IntegerField(
        read_only=True
    )
    date_of_created = serializers.DateTimeField(
        read_only=True
    )
    ratings = SerializerRating(
        many=True,
        read_only=True,
        source='rating_set'
    )
    average_rating = serializers.IntegerField(
        read_only=True
    )

    class Meta:
        model = Shop
        fields = "__all__"

    def to_representation(self, instance):
        if instance.indicate_address == False:
            instance.address = None

        return super().to_representation(instance)


class SerializerComplaint(serializers.ModelSerializer):
    screenshot = serializers.ImageField(
        required=False,
    )
    complaint_processed = serializers.BooleanField(
        read_only=True
    )

    class Meta:
        model = Complaint
        fields = "__all__"
