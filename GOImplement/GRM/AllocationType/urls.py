from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
  path('', views.AllocationTypeList.as_view(), name='Allocation Type'),
  path('<int:pk>/', views.AllocationTypeDetail.as_view(), name='Allocation Type'),

]
