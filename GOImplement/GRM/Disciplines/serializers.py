from rest_framework import serializers
from ..models import Disciplines

class DisciplinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplines
        fields = '__all__'