from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [
  path('ResourceExperience/', include('GOImplement.GRM.ResourceExperience.urls')),
  path('ProductSkills/', include('GOImplement.GRM.ProductSkills.urls')),
  path('ResourceProductSkills/', include('GOImplement.GRM.ResourceProductSkills.urls')),
  path('ResourceProjectExperience/', include('GOImplement.GRM.ResourceProjectExperience.urls')),
  path('ResourceTechnicalSkill/', include('GOImplement.GRM.ResourceTechnicalSkill.urls')),
  path('ResourceTraining/', include('GOImplement.GRM.ResourceTraining.urls')),
  path('TechnicalGroup/', include('GOImplement.GRM.TechnicalGroup.urls')),
  path('TechnicalSkills/', include('GOImplement.GRM.TechnicalSkills.urls')),
  path('AllocationType/', include('GOImplement.GRM.AllocationType.urls')),
  path('Countries/', include('GOImplement.GRM.Countries.urls')),
  path('Customers/', include('GOImplement.GRM.Customers.urls')),
  path('Disciplines/', include('GOImplement.GRM.Disciplines.urls')),
  path('Regions/', include('GOImplement.GRM.HexagonRegions.urlsRegions')),
  path('Teams/', include('GOImplement.GRM.HexagonRegions.urlsTeams')),
  path('Projects/', include('GOImplement.GRM.Projects.urls')),
  path('ProjectStatusCategoryTypes/', include('GOImplement.GRM.ProjectStatusCategoryTypes.urls')),
  path('ProjectStatusTypes/', include('GOImplement.GRM.ProjectStatusTypes.urls')),
  path('Resources/', include('GOImplement.GRM.Resources.urls')),
  path('Roles/', include('GOImplement.GRM.Roles.urls')),
  path('StatusTypes/', include('GOImplement.GRM.StatusTypes.urls')),
  path('Locations/', include('GOImplement.GRM.Locations.urls')),
  # path('PipelinePlanning/', include('GOImplement.GRM.PipelinePlanning.urls')),
  path('ProjectDemand/', include('GOImplement.GRM.ProjectDemand.urls')),
  path('Planning/', include('GOImplement.GRM.Planning.urls')),
  path('ProjectManagement/', include('GOImplement.GRM.ProjectManagement.urls')),
  path('ResourceManagement/', include('GOImplement.GRM.ResourceManagement.urls'))

]

urlpatterns = format_suffix_patterns(urlpatterns)

