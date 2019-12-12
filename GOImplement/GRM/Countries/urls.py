from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
  path('', views.CountriesList.as_view(), name='Countries List'),
  path('<int:pk>/', views.CountriesDetail.as_view(), name='Countries Detail'),

]
