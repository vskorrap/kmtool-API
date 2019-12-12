from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
  path('', views.ProjectsList.as_view(), name='Projects List'),
  # path('ProjectRegions/', views.ProjectsRegionData.as_view(), name='Projects Region Data List'),
  path('<int:pk>/', views.ProjectsDetail.as_view(), name='Projects Detail'),

]
