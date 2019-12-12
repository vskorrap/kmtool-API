from django.http import Http404
from requests import Response
from ..models import ResourceTechnicalSkills
from .serializers import ResourceTechnicalSkillSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ResourceTechnicalSkillList(APIView):
    def post(self, request, *args, **kwargs):
        file_serializer = ResourceTechnicalSkillSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        snippets = ResourceTechnicalSkills.objects.all()
        serializer = ResourceTechnicalSkillSerializer(snippets, many=True)
        return Response(serializer.data)

class ResourceTechnicalSkillDetail(APIView):
    def get_object(self, pk):
        try:
            return ResourceTechnicalSkills.objects.get(pk=pk)
        except ResourceTechnicalSkills.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ResourceTechnicalSkillSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ResourceTechnicalSkillSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


