from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from . import AuthenticationView


urlpatterns = [
    url('admin/', admin.site.urls),
    # url('login/',AuthenticationView.Authentication.as_view(),name='Authentication'),
    url(r'^GOImplement/GeneralDiscussion', include('GOImplement.GeneralDiscussion.urls')),
    url(r'^GRM/api/V1/Admin/', include('GOImplement.GRM.urls')),
    url(r'^file/', include('GOImplement.file_app.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	
