from django.urls import path
from . import views

urlpatterns = [
  path('addPlanning', views.Planning.as_view(), name='planning'),
]
