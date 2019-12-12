from django.urls import path


from . import views

urlpatterns = [
  path('', views.ResourceTechnicalSkillList.as_view(), name='ResourceTechnicalSkill List'),
  path('<int:pk>/', views.ResourceTechnicalSkillDetail.as_view(), name='ResourceTechnicalSkill Detail'),

]
