from rest_framework import serializers
from apps.demo.models import CAR


class CARSERIALIZER(serializers.ModelSerializer):
    class Meta:
        model = CAR
        fields = "__all__"
