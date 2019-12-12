from django.conf.urls import url
from .views import *
from django.urls import path
from .views import *
urlpatterns = [
  path('/api/V1/Questions/', GeneralDiscussionQuestion.as_view()),
  path('/api/V1/Answers/', GeneralDiscussionAnswer.as_view()),
  path('/api/V1/Questions/<int:pk>/', GetQuestionDetail.as_view(), name='Question Detail'),
  path('/api/V1/Highlights/', GetHighlightedResults.as_view(), name='Question Highlighted'),
  path('/api/V1/TEF/<int:pk>/', TefDiscussion.as_view(), name='TEF Questions'),
  path('/api/V1/TEF/', TefDiscussion.as_view(), name='Question Highlighted'),
]