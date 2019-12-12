from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
  path('', views.ResourcesList.as_view(), name='Resources List'),
  path('<int:pk>/', views.ResourcesDetail.as_view(), name='Resources Detail'),

]
