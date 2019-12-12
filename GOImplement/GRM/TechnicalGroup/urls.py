from django.urls import path


from . import views

urlpatterns = [
  path('', views.TechnicalGroupList.as_view(), name='TechnicalGroup List'),
  path('<int:pk>/', views.TechnicalGroupDetail.as_view(), name='TechnicalGroup Detail'),

]
