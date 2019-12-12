import logging

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from .models import File
from django.http import Http404
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': '131.163.160.58', 'port': 9200}], http_auth= ('admin', 'admin'))
index = "media"
type = "doc"

class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  # def post(self, request, *args, **kwargs):
  #   file_serializer = FileSerializer(data=request.data)
  #   if file_serializer.is_valid():
  #     file_serializer.save()
  #     return Response(file_serializer.data, status=status.HTTP_201_CREATED)
  #   else:
  #     return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  #
  #
  # def get(self, request, format=None):
  #     snippets = File.objects.all()
  #     serializer = FileSerializer(snippets, many=True)
  #     return Response(serializer.data)

  try:
      def post(self, request, *args, **kwargs):
          file_serializer = FileSerializer(data=request.data)
          if file_serializer.is_valid():
              file_serializer.save()
              return Response(file_serializer.data, status=status.HTTP_201_CREATED)
          else:
              return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      def get(self, request, format=None):
          query = {"query": {"match_all": {}}}
          response = []
          if ('search' in request.GET.keys()):
              query = {"query": {"match": {"content": {"query": request.GET['search'], "analyzer": "my_synonyms"}}},
                       "highlight": {"pre_tags": ["<span class='highlight'>"], "post_tags": ["</span>"],
                                     "fields": {"content": {}}}}
          for document in es.search(index=index, body=query)["hits"]["hits"]:
              data = {}
              if ('search' in request.GET.keys()):
                  data["content"] = document["highlight"]["content"]
              else:
                  data["content"] = document["_source"]["content"]
              data["filename"] = document["_source"]["file"]["filename"]
              data["category"] = document["_source"]["category"] if ('category' in document["_source"].keys()) else None
              data['timestamp'] = document["_source"]["file"]["indexing_date"]
              response.append(data)
          return Response(response)

  except Exception as e:
      logging.basicConfig(filename='GSCGlobalServices\LogFile.txt', level=logging.DEBUG)
      logging.error(str(e))

class FileDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return File.objects.get(pk=pk)
        except File.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = FileSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = FileSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

