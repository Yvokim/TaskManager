from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('tasks/', include('tasks.urls'))

    , ]

if settings.DEBUG:  # used in Django projects to serve static and media files during development.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
