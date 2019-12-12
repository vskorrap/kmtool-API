from rest_framework import serializers
from ..models import ProjectStatusTypes

class ProjectStatusTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStatusTypes
        fields = '__all__'


