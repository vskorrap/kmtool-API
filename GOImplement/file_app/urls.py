from django.conf.urls import url
from django.urls import path
from .views import FileView,FileDetail
urlpatterns = [
  url(r'^upload/$', FileView.as_view(), name='file-upload'),
  url(r'^upload/<int:pk>/$', FileDetail.as_view(), name='file-upload'),
  path('upload/<int:pk>/', FileDetail.as_view()),
]