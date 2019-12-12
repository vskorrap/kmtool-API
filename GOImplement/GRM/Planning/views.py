from .serializers import PlanningSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from ResourceManagement.models import *


class Planning(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data['project'])
        # data=request.data
        # PlanningRequest=ResourcePlanning.objects.filter(project=data['project'],resource=data['resource'])
        # print(PlanningRequest.query)
        planning = PlanningSerializer(data=request.data)
        if planning.is_valid():
            planning.save()
            return Response(planning.data, status=status.HTTP_201_CREATED)
        else:
            return Response(planning.errors, status=status.HTTP_400_BAD_REQUEST)