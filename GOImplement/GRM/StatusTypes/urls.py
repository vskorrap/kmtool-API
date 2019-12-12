from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
  path('', views.StatusTypesList.as_view(), name='StatusTypes List'),
  path('<int:pk>/', views.StatusTypesDetail.as_view(), name='StatusTypes Detail'),

]
