from .serializers import ProjectDemandSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Demand(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data['project'])
        data=request.data
        # PlanningRequest=ResourcePlanning.objects.filter(project=data['project'],resource=data['resource'])
        # print(PlanningRequest.query)
        demand = ProjectDemandSerializer(data=request.data)
        if demand.is_valid():
            demand.save()
            return Response(demand.data, status=status.HTTP_201_CREATED)
        else:
            return Response(demand.errors, status=status.HTTP_400_BAD_REQUEST)