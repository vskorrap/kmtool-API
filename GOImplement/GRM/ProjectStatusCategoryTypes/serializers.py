from rest_framework import serializers
from ..models import ProjectStatusCategoryTypes

class ProjectStatusCategoryTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStatusCategoryTypes
        fields = '__all__'

