from rest_framework import serializers
from ..models import TechnicalSkills

class TechnicalSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalSkills
        fields = '__all__'