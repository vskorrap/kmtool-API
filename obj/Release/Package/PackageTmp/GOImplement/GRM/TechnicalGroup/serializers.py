from rest_framework import serializers
from ..models import TechnicalGroup

class TechnicalGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalGroup
        fields = '__all__'