from django.urls import path


from . import views

urlpatterns = [
  path('', views.ResourceProductSkillsList.as_view(), name='ResourceProductSkills List'),
  path('<int:pk>/', views.ResourceProductSkillsDetail.as_view(), name='ResourceProductSkills Detail'),

]
