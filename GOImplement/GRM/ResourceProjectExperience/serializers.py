from rest_framework import serializers
from ..models import ResourceProjects

class ResourceProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceProjects
        fields = '__all__'
