from django.conf.urls import patterns
from django.conf.urls import url

from .views import FileList
from .views import FileUpload
from .views import FileInfo


urlpatterns = patterns('',
	
	url(r'^files/$', FileList.as_view(), name='file-list'),
	url(r'^files/add/$', FileUpload.as_view(), name='file-upload'),
	url(r'^files/(?P<slug>[a-z0-9\-]+)/info/$', FileInfo.as_view(), name='file-info'),
	
)
