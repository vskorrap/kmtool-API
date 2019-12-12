from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
  path('', views.ProjectStatusCategoryTypesList.as_view(), name='Project Status Category List'),
  path('<int:pk>/', views.ProjectStatusCategoryTypesDetail.as_view(), name='Project Status Category Detail'),

]
