from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('intro.urls')),
    path('file_upload/', include('file_upload.urls')),
]

if settings.DEBUG==True:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
