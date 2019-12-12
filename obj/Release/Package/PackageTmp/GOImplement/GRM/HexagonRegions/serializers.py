from rest_framework import serializers
from ..models import Teams

class HexagonRegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ('id','teamName')