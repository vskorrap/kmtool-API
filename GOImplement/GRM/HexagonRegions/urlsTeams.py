from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
  path('', views.HexagonTeamsList.as_view(), name='Teams'),
  # path('<int:pk>/', views.HexagonRegionsDetail.as_view(), name='Hexagon Region'),

]




