from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include(('simplemooc.core.urls', 'core'), namespace='core')),
    path('cursos/', include(('simplemooc.accounts.urls', 'accounts'), namespace='accounts')),
    path('conta/', include(('simplemooc.courses.urls', 'courses'), namespace='courses')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)