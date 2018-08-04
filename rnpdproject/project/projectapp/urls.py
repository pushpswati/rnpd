from django.conf.urls import url
from projectapp import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
url(r'^rnpd/upload',views.Rnpd_upload.as_view(),name='rnpd_upload'),
url(r'^numplateresult',views.NumplateResultImageUpload.as_view(),name='numplateresult'),


]
if settings.DEBUG:
       urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

