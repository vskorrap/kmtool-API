from rest_framework import serializers
from .models import *


class DiscussionForum_QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionForum_Questions
        fields = '__all__'


class DiscussionForum_AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionForum_Answers
        fields = '__all__'