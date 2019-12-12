from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
  path('', views.CustomersList.as_view(), name='Customers List'),
  path('<int:pk>/', views.CustomersDetail.as_view(), name='Customers Detail'),

]
