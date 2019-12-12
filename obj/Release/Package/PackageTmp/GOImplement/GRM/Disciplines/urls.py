from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
  path('', views.DisciplinesList.as_view(), name='Disciplines List'),
  path('<int:pk>/', views.DisciplinesDetail.as_view(), name='Disciplines Detail'),

]
