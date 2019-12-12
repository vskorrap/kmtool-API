from rest_framework import serializers
from ..models import ProductSkills

class ProductSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSkills
        fields = '__all__'