from django.urls import path
from . import views

urlpatterns = [
  path('utilization/', views.Utilization.as_view(), name='Soft Book'),
  path('resourceAssignement/',views.ResourceAssisgnement.as_view(),name='Resource Assignment')
]
