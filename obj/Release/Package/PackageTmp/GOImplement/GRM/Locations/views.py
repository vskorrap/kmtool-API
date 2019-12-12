from django.http import Http404
from requests import Response
from ..models import Locations
from .serializers import LocationsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import *

class LocationsList(APIView):
    def post(self, request,startdate,enddate, *args, **kwargs):
        file_serializer = LocationsSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        snippets = Locations.objects.all()
        serializer = LocationsSerializer(snippets, many=True)
        return Response(serializer.data)

class LocationsDetail(APIView):
    def get_object(self, pk):
        try:
            return Locations.objects.get(pk=pk)
        except Locations.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = LocationsSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = LocationsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


