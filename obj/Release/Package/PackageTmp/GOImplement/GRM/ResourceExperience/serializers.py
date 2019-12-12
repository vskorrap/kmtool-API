from rest_framework import serializers
from ..models import ResourceExperience

class ResourceExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceExperience
        fields = '__all__'