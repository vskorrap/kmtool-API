from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from GOImplement.GRM.utils import dictfetchall
from django.db.models import F,Q,Sum
from ..Resources import serializers
from ..models import *
from datetime import datetime,date


class Utilization(APIView):
    def get(self,format=None):
        data = list(ResourcePlanning.objects.filter().values('resource','percentage','endDate'))
        dataDictionary = dict()
        response = {}
        response["resources"] = []
        for object in data:
            if datetime.strptime(str(date.today()), '%Y-%m-%d') <= datetime.strptime(str(object["endDate"]), '%Y-%m-%d'):
                id = object["resource"]
                percentage = object["percentage"]
                if id not in dataDictionary:
                    dataDictionary[id] = percentage
                else:
                    dataDictionary[id]+=percentage

        for object in data:
            if dataDictionary[object["resource"]] <= 0.5 :
                resources = Resources.objects.filter(pk=object["resource"]).values('firstName','surName',Team=F('team__teamName'),Discipline=F('discipline__discipline'))
                resource = {}
                resource["discipline"] = resources[0]["Discipline"]
                resource["team"] = resources[0]["Team"]
                resource["name"] = resources[0]["firstName"] + " " + resources[0]["surName"]
                resource["id"] = object["resource"]
                response["resources"].append(resource)
        return Response(response)

class ResourceAssisgnement(APIView):
    def get(self,format=None):
        resourceAssignment=[]
        regions=Teams.objects.filter(region=True).values('id','teamName')
        countries=Countries.objects.filter(hexRegion__region=True).values('country','abbrev','hexRegion')
        cursor = connection.cursor()
        cursor.execute('GetResourceAssignement')
        resourceAssignmentCount = dictfetchall(cursor)
        # resource=Resources.objects.filter(~Q(allocationType__allocationType='Never Include'),statusType__statusType='Active')\
        #     .values('firstName','surName','resourceplanning__project__country__hexRegion__teamName')\
        #     .annotate(total=Sum('resourceplanning__percentage'))
        for region in regions:
            data={}
            data["region"]=region["teamName"]
            data["countries"]=list(filter(lambda country:country['hexRegion']==region["id"],countries))
            resourceCount=list(filter(lambda count:count['teamName']==region["teamName"],resourceAssignmentCount))
            if len(resourceCount) == 0:
                data["count"]=0
            else:
                for res in resourceCount:
                    data["count"]=round(res["count"],2)
            resourceAssignment.append(data)
        return Response(resourceAssignment)
