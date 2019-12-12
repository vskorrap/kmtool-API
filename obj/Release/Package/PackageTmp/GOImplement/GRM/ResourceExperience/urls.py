from django.urls import path


from . import views

urlpatterns = [
  path('', views.ResourceExperienceList.as_view(), name='ResourceExperience List'),
  path('<int:pk>/', views.ResourceExperienceDetail.as_view(), name='ResourceExperience Detail'),

]
