from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
  path('', views.HexagonRegionsList.as_view(), name='Regions'),
  # path('<int:pk>/', views.HexagonRegionsDetail.as_view(), name='Hexagon Region'),

]




