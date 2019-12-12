from rest_framework import serializers
from ..models import StatusTypes

class StatusTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusTypes
        fields = '__all__'