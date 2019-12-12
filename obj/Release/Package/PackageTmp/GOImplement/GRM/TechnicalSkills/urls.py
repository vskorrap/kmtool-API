from django.urls import path


from . import views

urlpatterns = [
  path('', views.TechnicalSkillsList.as_view(), name='TechnicalSkills List'),
  path('<int:pk>/', views.TechnicalSkillsDetail.as_view(), name='TechnicalSkills Detail'),

]
