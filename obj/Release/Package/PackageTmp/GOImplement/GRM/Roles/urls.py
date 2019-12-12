from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
  path('', views.RolesList.as_view(), name='Roles List'),
  path('<int:pk>/', views.RolesDetail.as_view(), name='Roles Detail'),

]
