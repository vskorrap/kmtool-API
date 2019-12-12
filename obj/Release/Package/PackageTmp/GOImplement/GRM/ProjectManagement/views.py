from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum,F,Count
from ..models import *
from ..Projects.serializers import ProjectsSerializer
from ..Disciplines.serializers import DisciplinesSerializer
from ..Customers.serializers import CustomersSerializer
from ..Countries.serializers import CountriesSerializer
from ..Resources.serializers import ResourcesSerializer
from ..ProjectStatusTypes.serializers import ProjectStatusTypesSerializer
from ..ProjectDemand.serializers import ProjectDemandSerializer
from django.http import Http404


from rest_framework import serializers
from ..models import Locations

class ResourcePlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourcePlanning
        fields = '__all__'


class ProjectManagement(APIView):
    def get(self,request, format=None):
        projectSummary=[]
        ProjectSummary = Projects.objects.values('id', 'projectName', 'startDate', 'endDate','projectStatus__projectStatus', 'customer__customer','country__country', 'createdDate','budgetHours')
        demandData=ProjectDemand.objects.values('project',disciplineName=F('discipline__discipline'), teamName=F('team__teamName')).annotate(hours=Sum('ftes')*8)
        assignedData=ResourcePlanning.objects.values('project',disciplineName=F('discipline__discipline')).annotate(hours=Sum('percentage')*8,ResourceCount=Count('resource'))
        for project in ProjectSummary:
            data={}
            data["id"]=project["id"]
            data["projectName"]=project["projectName"]
            data["startDate"] = project["startDate"]
            data["endDate"] = project["endDate"]
            data["projectStatus"] = project["projectStatus__projectStatus"]
            data["customer"] = project["customer__customer"]
            data["country"] = project["country__country"]
            data["createdDate"] = project["createdDate"]
            data["budgetHours"] = project["budgetHours"]
            demandList=list(filter(lambda demand:demand['project']==project["id"],demandData))
            assignedList = list(filter(lambda asigned: asigned['project'] == project["id"], assignedData))
            data["demandData"] = demandList
            data["assignedData"] = assignedList
            projectSummary.append(data)
        return Response(projectSummary)

class ProjectManagementDetail(APIView):
    # permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Projects.objects.get(pk=pk)
        except Projects.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        response = list(Projects.objects.values('projectName','startDate','endDate','budgetHours', productName=F('product__discipline'),customerName=F('customer__customer'),countryName=F('country__country'),projectmanager=F('projectManager__firstName')).filter(pk=pk))
        response[0]["projectManager"] = response[0]["projectmanager"]
        response[0].pop("projectmanager")
        demandData = ProjectDemand.objects.filter(project=pk)
        demandSerializer = ProjectDemandSerializer(demandData,many=True)
        response[0]["demandData"] = []
        for project in demandSerializer.data:
            data = {}
            data["discipline"] = project["discipline"]
            data["productSkills"] = project["productSkills"]
            data["technicalSkills"] = project["technicalSkills"]
            data["startDate"] = project["startDate"]
            data["endDate"] = project["endDate"]
            data["noOfFTE"] = project["ftes"]
            data["team"] = project["team"]
            response[0]["demandData"].append(data)
        resourceData = ResourcePlanning.objects.filter(project=pk)
        resourcePlanningSerializer = ResourcePlanningSerializer(resourceData, many=True)
        response[0]["resourceData"] = []
        for resouce in resourcePlanningSerializer.data:
            data = {}
            data["resource"] = resouce["resource"]
            data["role"] = resouce["role"]
            data["discipline"] = resouce["discipline"]
            data["chargeTo"] = resouce["chargeTo"]
            data["support"] = resouce["support"]
            data["crossCharging"] = resouce["crossCharging"]
            data["onSite"] = resouce["onSite"]
            data["startDate"] = resouce["startDate"]
            data["endDate"] = resouce["endDate"]
            response[0]["resourceData"].append(data)

        return Response(response)

