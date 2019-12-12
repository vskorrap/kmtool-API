from rest_framework import serializers
from ..models import AllocationTypes

class AllocationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllocationTypes
        fields = '__all__'