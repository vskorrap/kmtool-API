from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
  path('', views.ProjectStatusTypesList.as_view(), name='Project Status Types List'),
  path('<int:pk>/', views.ProjectStatusTypesDetail.as_view(), name='Project Status Types Detail'),

]
