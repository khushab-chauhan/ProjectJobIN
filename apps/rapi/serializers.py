from rest_framework import serializers
from apps.rapi.models import CAR

class CARSERIALIZERS(serializers.ModelSerializer):
    class Meta:
        model = CAR
        fields = "__all__"