from rest_framework import serializers

from .models import Complain, Support


class ComplainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complain
        fields = "__all__"


class SupportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Support
        fields = "__all__"
