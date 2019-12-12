from rest_framework import serializers
from ..models import ProjectDemand

class ProjectDemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDemand
        fields = ('project', 'discipline','productSkills','technicalSkills','ftes','startDate','endDate','team','Version')