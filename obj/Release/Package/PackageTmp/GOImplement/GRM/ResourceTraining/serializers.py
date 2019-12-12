from rest_framework import serializers
from ..models import ResourceTrainings

class ResourceTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceTrainings
        fields = '__all__'