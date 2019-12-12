import json
from django.core import serializers
from django.http import Http404
from requests import Response
from ..models import *
from .serializers import ProjectsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from datetime import date


class ProjectsList(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        real_data = {}
        real_data["customer"] = data["customer"]
        real_data["projectName"] = data["projectName"]
        real_data["startDate"] = data["startDate"]
        real_data["endDate"] = data["endDate"]
        real_data["product"] = data["product"]
        real_data["status"] = data["status"]
        real_data["defAllocation"] = data["defAllocation"]
        real_data["chargeable"] = data["chargeable"]
        real_data["sfdcOppName"] = data["sfdcOppName"]
        real_data["country"] = data["country"]
        real_data["projectStatus"] = data["projectStatus"]
        real_data["adminUse"] = data["adminUse"]
        real_data["sfdcId"] = data["sfdcId"]
        real_data["weeksDuration"] = data["weeksDuration"]
        real_data["probability"] = data["probability"]
        real_data["docType"] = data["docType"]
        real_data["adminLock"] = data["adminLock"]
        real_data["createdDate"] = date.today()
        real_data["budgetHours"] = data["budgetHours"]

        file_serializer = ProjectsSerializer(data=real_data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        snippets = Projects.objects.all()
        serializer = ProjectsSerializer(snippets, many=True)
        return Response(serializer.data)

class ProjectsDetail(APIView):
    # permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Projects.objects.get(pk=pk)
        except Projects.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProjectsSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        data = request.data
        real_data = {}
        real_data["customer"] = data["customer"]
        real_data["projectName"] = data["projectName"]
        real_data["startDate"] = data["startDate"]
        real_data["endDate"] = data["endDate"]
        real_data["product"] = data["product"]
        real_data["status"] = data["status"]
        real_data["defAllocation"] = data["defAllocation"]
        real_data["chargeable"] = data["chargeable"]
        real_data["sfdcOppName"] = data["sfdcOppName"]
        real_data["country"] = data["country"]
        real_data["projectStatus"] = data["projectStatus"]
        real_data["adminUse"] = data["adminUse"]
        real_data["sfdcId"] = data["sfdcId"]
        real_data["weeksDuration"] = data["weeksDuration"]
        real_data["probability"] = data["probability"]
        real_data["docType"] = data["docType"]
        real_data["adminLock"] = data["adminLock"]
        real_data["createdDate"] = snippet["createdDate"]
        real_data["budgetHours"] = data["budgetHours"]
        serializer = ProjectsSerializer(snippet, data=real_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class ProjectsRegionData(APIView):
#     def get(self,request,format=None):
#         projects = list(Projects.objects.filter(fkprojectstatus__blnactivetype=1).values('strprojectname','pkid','fkcountry__strcountry'))
#         countries = list(Projects.objects.values('strcountry','fkhexregion__strregionname'))
#         response = []
#         for country in countries:
#             data = {}
#             data["strcountry"] = country["strcountry"]
#             data["strRegionName"] = country["fkhexregion__strregionname"]
#             if(country["fkhexregion__strregionname"]=="SA"):
#                 data["colour"] = "green"
#             if (country["fkhexregion__strregionname"] == "EMIA"):
#                 data["colour"] = "blue"
#             if (country["fkhexregion__strregionname"] == "NA"):
#                 data["colour"] = "red"
#             if (country["fkhexregion__strregionname"] == "APAC"):
#                 data["colour"] = "yellow"
#             if (country["fkhexregion__strregionname"] == "china"):
#                 data["colour"] = "black"
#
#             data["projects"] = []
#
#             for project in projects:
#                 if(project["fkcountry__strcountry"]==data["strcountry"]):
#                     project_data = {}
#                     project_data["project_pkid"] = project["pkid"]
#                     project_data["project_name"] = project["strprojectname"]
#                     data["projects"].append(project_data)
#             response.append(data)
#         return Response(response)
