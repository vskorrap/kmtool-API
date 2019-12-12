from django.urls import path
from . import views

urlpatterns = [
  path('summary/', views.ProjectManagement.as_view(), name='Project Demand'),
  path('<int:pk>/', views.ProjectManagementDetail.as_view(), name='Project Management Detail'),
]
