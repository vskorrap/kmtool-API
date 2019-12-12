from rest_framework import serializers
from ..models import ResourceProductSkills

class ResourceProductSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceProductSkills
        fields = '__all__'