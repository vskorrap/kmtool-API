import logging
from datetime import datetime

from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from elasticsearch import Elasticsearch
from .models import *

es = Elasticsearch([{'host': '131.163.160.58', 'port': 9200}], http_auth=('admin', 'admin'))
index = "discussion_cafe"
type = "Discussion"


class GeneralDiscussionQuestion(APIView):
    try:
        def get(self, request, format=None):
            response = []
            for questions in es.search(index=index, body={"query":{"match":{"Category":"General"}}})["hits"]["hits"]:
                data = {}
                data["Question"] = questions["_source"]["Question"]
                data["Answers"] = questions["_source"]["Answers"]
                data["pkid"] = questions["_source"]["pkid"]
                response.append(data)

            return Response(response)

        def post(self, request, *args, **kwargs):
            data = request.data
            data["Subject"] = "NULL"
            data["Timestamp"] = datetime.now()
            file_serializer = DiscussionForum_QuestionsSerializer(data=data)
            if file_serializer.is_valid():
                file_serializer.save()
                data["Answers"] = []
                data["Category"] = "General"
                data["pkid"] = file_serializer.data["id"]
                print(data)
                elasticdata = es.index(index=index, doc_type=type, body=data)
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logging.basicConfig(filename='GOImplement\LogFile.txt', level=logging.DEBUG)
        logging.error(str(e))


class GeneralDiscussionAnswer(APIView):
    try:
        def post(self, request, *args, **kwargs):
            file_serializer = DiscussionForum_AnswersSerializer(data=request.data)
            if file_serializer.is_valid():
                file_serializer.save()
                questionid = \
                es.search(index=index, body={"query": {"match": {"pkid": request.data["fkQuestion"]}}})["hits"]["hits"][
                    0]["_id"]
                ans = request.data["Answer"]
                add_answer = {
                    "script": {"source": "ctx._source.Answers.add(params.new_ans)", "params": {"new_ans": ans}}}
                elasticdata = es.update(index=index, doc_type=type, id=questionid, body=add_answer)
                return Response(elasticdata, status=status.HTTP_201_CREATED)
            else:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        logging.basicConfig(filename='GOImplement\LogFile.txt', level=logging.DEBUG)
        logging.error(str(e))


class GetQuestionDetail(APIView):
    def get(self, request, pk, format=None):
        data = {}
        data["question"] = \
        es.search(index=index, body={"query": {"match": {"pkid": pk}}})["hits"]["hits"][0]["_source"]["Question"]
        data["answer"] = es.search(index=index, body={"query": {"match": {"pkid": pk}}})["hits"]["hits"][0]["_source"][
            "Answers"]
        return Response(data)


class GetHighlightedResults(APIView):
    def get(self, request, format=None):
        # text = request.data["Text"]
        text = request.GET.get('text')
        response = []
        if text == "" :
            for questions in es.search(index=index, body={"size": 10000, "query": {"match_all": {}}})["hits"]["hits"]:
                data = {}
                data["Question"] = questions["_source"]["Question"]
                data["Answers"] = questions["_source"]["Answers"]
                data["pkid"] = questions["_source"]["pkid"]
                data["Timestamp"] = questions["_source"]["Timestamp"]
                data["Category"] = questions["_source"]["Category"]
                response.append(data)

            return Response(response)

        else:

            for question in es.search(index=index, doc_type=type, body={"query": {"bool": {
                "must": [{"match_phrase_prefix": {"Question": {"query": text, "analyzer": "my_synonyms"}}},
                         ]}}, "highlight": {"pre_tags": ["<strong>"],
                                                                              "post_tags": ["</strong>"],
                                                                              "fields": {"Question": {}}}})["hits"]["hits"]:
                data = {}
                data["Question"] = question["_source"]["Question"]
                data["Pkid"] = question["_source"]["pkid"]
                data["Highlights"] = question["highlight"]["Question"]
                data["Category"] = question["_source"]["Category"]
                data["Answers"] = question["_source"]["Answers"]
                response.append(data)

        return Response(response)


class TefDiscussion(APIView):

    def get(self, request, format=None):
        response = []
        for questions in es.search(index=index, body={"size": 10000, "query": {"match": {"Category": "TEF"}}})["hits"][
            "hits"]:
            data = {}
            data["Question"] = questions["_source"]["Question"]
            data["Answers"] = questions["_source"]["Answers"]
            data["pkid"] = questions["_source"]["pkid"]
            data["AskedBy"] = questions["_source"]["Sender"]
            response.append(data)
        return Response(response)

class TefDiscussion(APIView):

    def get(self, request, pk, format=None):
        response = []
        response_count = {}
        # page_num = request.data['page']
        filter = request.GET.get('time')
        page_num = pk
        questions = es.search(index=index, body={"size": 10000, "query": {"match": {"Category": "TEF"}}})["hits"]["hits"]
        count = es.search(index=index, body={"size": 10000, "query": {"match": {"Category": "TEF"}}})["hits"]["total"]
        if filter == '24 Hours':
            time = datetime.datetime.now()- datetime.timedelta(days=1)
            print(time)
            questions = es.search(index=index, body={"size": 10000, "query":
                {"bool":{
                    "must":[
                {"match":
                     {"Category": "TEF"}
                },
                {
                 "range":{
                     "Timestamp":{
                         "gte":time,
                         "lte":datetime.datetime.now()
                     }
                 }
                }
            ]}}}
        )["hits"]["hits"]
            count = es.search(index=index, body={"size": 10000, "query":
                {"bool":{
                    "must":[
                {"match":
                     {"Category": "TEF"}
                },
                {
                 "range":{
                     "Timestamp":{
                         "gte":time,
                         "lte":datetime.datetime.now()
                     }
                 }
                }
            ]}}}
        )["hits"]["total"]
        elif filter == 'past week':
            time = datetime.datetime.now()- datetime.timedelta(days=7)
            print(time)
            questions = es.search(index=index, body={"size": 10000, "query":
                {"bool":{
                    "must":[
                {"match":
                     {"Category": "TEF"}
                },
                {
                 "range":{
                     "Timestamp":{
                         "gte":time,
                         "lte":datetime.datetime.now()
                     }
                 }
                }
            ]}}}
        )["hits"]["hits"]
            count = es.search(index=index, body={"size": 10000, "query":
                {"bool": {
                    "must": [
                        {"match":
                             {"Category": "TEF"}
                         },
                        {
                            "range": {
                                "Timestamp": {
                                    "gte": time,
                                    "lte": datetime.datetime.now()
                                }
                            }
                        }
                    ]}}}
                              )["hits"]["total"]
        elif filter == 'past month':
            time = datetime.datetime.now()- datetime.timedelta(days=30)
            print(time)
            questions = es.search(index=index, body={"size": 10000, "query":
                {"bool":{
                    "must":[
                {"match":
                     {"Category": "TEF"}
                },
                {
                 "range":{
                     "Timestamp":{
                         "gte":time,
                         "lte":datetime.datetime.now()
                     }
                 }
                }
            ]}}}
        )["hits"]["hits"]
            count = es.search(index=index, body={"size": 10000, "query":
                {"bool": {
                    "must": [
                        {"match":
                             {"Category": "TEF"}
                         },
                        {
                            "range": {
                                "Timestamp": {
                                    "gte": time,
                                    "lte": datetime.datetime.now()
                                }
                            }
                        }
                    ]}}}
                              )["hits"]["total"]
        if page_num <= (count / 10) + 1:
            paginator = Paginator(questions, 10)
            page = paginator.page(page_num)
            response_count["Count"] = count
            for i in page.object_list:
                data = {}
                data["Question"] = i["_source"]["Question"]
                data["Answers"] = i["_source"]["Answers"]
                data["pkid"] = i["_source"]["pkid"]
                data["AskedBy"] = i["_source"]["Sender"]
                data["Category"] = i["_source"]["Category"]
                response.append(data)
            response_count["Response"]=response
            return Response(response_count)
        return Response([])


