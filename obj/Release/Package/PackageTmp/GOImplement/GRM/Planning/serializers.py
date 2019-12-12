from rest_framework import serializers
from ..models import ResourcePlanning

class PlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourcePlanning
        fields = ('project', 'resource','role','discipline','chargeTo','support','crossCharging','onSite','startDate','endDate','percentage')