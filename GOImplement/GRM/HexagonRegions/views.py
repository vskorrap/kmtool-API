from django.http import Http404
from requests import Response
from ..models import Teams
from .serializers import HexagonRegionsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HexagonRegionsList(APIView):

    def get(self, request, format=None):
        snippets = Teams.objects.filter(region=True)
        serializer = HexagonRegionsSerializer(snippets, many=True)
        return Response(serializer.data)

# class HexagonRegionsDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Tblhexagonregions.objects.get(pk=pk)
#         except Tblhexagonregions.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = HexagonRegionsSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = HexagonRegionsSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class HexagonTeamsList(APIView):
    def get(self, request, format=None):
        snippets = Teams.objects.all()
        serializer = HexagonRegionsSerializer(snippets, many=True)
        return Response(serializer.data)

# class HexagonTeamsDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Tblhexagonregions.objects.get(pk=pk)
#         except Tblhexagonregions.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = HexagonRegionsSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = HexagonRegionsSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


