from rest_framework import serializers
from ..models import ResourceTechnicalSkills

class ResourceTechnicalSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceTechnicalSkills
        fields = '__all__'