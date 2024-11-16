from rest_framework import serializers

from .models import Complain, SupportMessage


class ComplainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complain
        finds = "__all__"


class SupportMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SupportMessage
        finds = "__all__"
