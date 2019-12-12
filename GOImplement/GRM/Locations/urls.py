from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
  path('', views.LocationsList.as_view(), name='Locations'),
  path('<int:pk>/', views.LocationsDetail.as_view(), name='Location'),

]
