from django.urls import path


from . import views

urlpatterns = [
  path('', views.ResourceTrainingList.as_view(), name='ResourceTraining List'),
  path('<int:pk>/', views.ResourceTrainingDetail.as_view(), name='ResourceTraining Detail'),

]
