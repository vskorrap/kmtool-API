from django.urls import path


from . import views

urlpatterns = [
  path('', views.ProductSkillsList.as_view(), name='ProductSkills List'),
  path('<int:pk>/', views.ProductSkillsDetail.as_view(), name='ProductSkills Detail'),

]
