from django.urls import path
from . import views

urlpatterns = [
  path('addProjectDemand', views.Demand.as_view(), name='Project Demand'),
]
