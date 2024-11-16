from rest_framework import serializers

from .models import Complain, Support


class ComplainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complain
        finds = "__all__"


class SupportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Support
        finds = "__all__"
